# Fraud Detection Project

## Project Overview

This project focuses on detecting fraudulent transactions in e-commerce and credit card data. It involves data preprocessing, exploratory data analysis (EDA), feature engineering, model training, and deployment of a web application using Flask and Dash for visualizing fraud insights.

## Directory Structure

```
/FraudDetection
│
├── /scripts
│   ├── preprocessing.py      # Functions for data preprocessing and feature engineering
│   ├── eda.py                # Functions for exploratory data analysis
│   ├── model_training.py      # Functions for training machine learning models
|   └── model_loader.py     # Loads the model from MLflow
│├── app/
│   ├── __init__.py
│   ├── main.py             # Entry point for Flask app
│   ├── endpoints.py        # Defines Flask API endpoints
│   ├── data_loader.py      # Handles data loading and processing
│   ├── logging_config.py   # Configures logging
│   └── predictions.py      # Contains prediction-related functions
├── dashboard/
│   ├── __init__.py
│   ├── layout.py           # Defines Dash layout and components
│   ├── callbacks.py        # Contains Dash callbacks for interactivity
├── models/
│
├── /notebooks
│   ├── eda_fraud.ipynb       # Jupyter Notebook for fraud dataset analysis
│   └── eda_credit_card.ipynb  # Jupyter Notebook for credit card data analysis
│
|── Dockerfile
├── requirements.txt           # List of required Python packages
└── README.md                  # Project documentation
```

## Key Components

### Scripts

- **preprocessing.py**: Functions for loading, cleaning, and merging datasets; converting IP addresses; feature engineering; scaling, and encoding.
- **eda.py**: Functions for performing EDA including visualizing distributions, correlations, and geographic patterns in fraudulent transactions.
- **model_training.py**: Contains code for training the fraud detection model and saving it using MLflow.

### Notebooks

- **eda_fraud.ipynb**: Analyzes the fraud dataset with steps for loading data, preprocessing, feature engineering, and EDA.
- **eda_credit_card.ipynb**: Focuses on credit card transaction data analysis and examines transaction class distribution and correlations.

### Flask & Dash Application

- **Flask API**: Provides endpoints for fraud prediction model, summary statistics, fraud trends, and geographic fraud analysis.
- **Interactive Dashboard**: Built with Dash to visualize insights, including:
  - Total transactions, fraud cases, and fraud percentages.
  - Line chart showing fraud cases over time.
  - Geographic analysis of fraud occurrences.
  - Bar chart comparing fraud cases across devices and browsers.

## How to Run

### Installation

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. To run the Flask app with the embedded Dash dashboard:

   ```bash
   python app/main.py
   ```

2. Access the application at `http://localhost:5000`.

### Docker

To run the application using Docker:

1. Build the Docker image:

   ```bash
   docker build -t fraud-detection-dashboard .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 fraud-detection-dashboard
   ```

## Logging

The application integrates Flask-Logging to track incoming requests, errors, and predictions. Logs can be found in the terminal or redirected to a file as configured.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or new features.

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.
