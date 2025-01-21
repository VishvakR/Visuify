from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Path to the dataset
Data_file = "datasets/sample_data.csv"
df = pd.read_csv(Data_file)

@app.route('/')
def home():
    columns = df.columns.tolist()
    return render_template('index.html', columns=columns)
@app.route('/visualize', methods=['POST'])
def visualize():
    graph_data = request.form.to_dict(flat=False)
    graphs = []  # To store image paths
    line_data = []  # To store data for Chart.js
    totals = []
    statistics = {}

    for i in range(len(graph_data.get('x-axis', []))):
        x_col = graph_data['x-axis'][i]
        y_col = graph_data['y-axis'][i]

        if x_col and y_col:
            # Generate image for the graph using matplotlib
            img_path = f"static/plot_{i + 1}.png"
            plt.figure(figsize=(6, 4))
            plt.plot(df[x_col], df[y_col], marker='o', label=f"{x_col} vs {y_col}")
            plt.title(f"Graph {i + 1}: {x_col} vs {y_col}")
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.legend()
            plt.grid()
            plt.savefig(img_path)
            plt.close()
            graphs.append(img_path)

            # Collect X and Y values for the line chart (Chart.js)
            x_values = df[x_col].tolist()
            y_values = df[y_col].tolist()
            line_data.append({
                "x": x_values,
                "y": y_values,
                "x_label": x_col,
                "y_label": y_col
            })

            # Calculate totals
            total = float(df[y_col].sum())
            totals.append((y_col, total))

            # Calculate statistics
            stats = {
                "mean": df[y_col].mean(),
                "median": df[y_col].median(),
                "std_dev": df[y_col].std()
            }
            statistics[y_col] = stats

    return render_template('visualization.html', graphs=graphs, line_data=line_data, totals=totals, statistics=statistics)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    global df
    if request.method == 'POST':
        file = request.files['file']
        if not file.filename.lower().endswith('.csv'):
            return render_template('upload.html', message="Only CSV files are allowed.")
        file_path = os.path.join('datasets', file.filename)
        file.save(file_path)
        df = pd.read_csv(file_path)
        return render_template('upload.html', message="File uploaded successfully! Go back to visualize your data.")
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=True)
