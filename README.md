# Visuify

# Data Visualization Dashboard

This project is a web-based data visualization dashboard built using Flask and Python. It allows users to upload a CSV dataset, select columns for visualizing data, and generate graphical visualizations in the form of plots and interactive charts.

## Features

- **Upload Dataset**: Users can upload a CSV file to analyze.
- **Visualization**: Users can select columns from the dataset to generate line graphs and interactive charts using Chart.js.
- **Statistical Analysis**: Calculates and displays mean, median, and standard deviation for selected Y-axis columns.
- **Data Summary**: Displays total values for the selected Y-axis columns.

## Technologies Used

- **Flask**: A micro web framework used to build the application.
- **Pandas**: Used for data manipulation and analysis.
- **Matplotlib**: Used for generating graphs.
- **Chart.js**: JavaScript library for creating interactive charts.
- **HTML, CSS, and Bootstrap**: Used for front-end styling and responsiveness.

## Installation
-pip install -r requirements.txt

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Steps to Run the Application

1. Clone the repository to your local machine:
   ```bash
   git clone <https://github.com/VishvakR/Visuify.git>
   cd <repository-directory>
2. Install the required dependencies:

   -pip install -r requirements.txt

3. Run the Flask application:
   
   -python app.py
   
4.Open a web browser and go to:
   -http://127.0.0.1:5000/

# Flie Structure:
/project-directory
    /datasets                # Contains the CSV files to upload
    /static                  # Static files (images, CSS, JS)
        /images
        /styles.css
        /favicon
    /templates               # HTML files
        index.html
        visualization.html
        upload.html
    app.py                    # Flask application code
    requirements.txt          # List of Python dependencies
    README.md                 # Project documentation


 Visuify is an interactive data visualization dashboard that allows users to upload CSV datasets, select columns, and generate dynamic graphs and statistical insights. Built with Flask, Pandas, and Chart.js, it provides an intuitive interface for exploring data with customizable visualizations and real-time statistical calculations.
