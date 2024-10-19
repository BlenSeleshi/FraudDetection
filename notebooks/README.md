# README for Fraud Detection Project

## Project Overview

This project focuses on detecting fraudulent transactions in e-commerce and credit card data. It includes data preprocessing, exploratory data analysis (EDA), feature engineering, and model training to improve fraud detection accuracy.

## Directory Structure

```
/fraud_detection_project
│
├── /scripts
│   ├── preprocessing.py      # Script for data preprocessing
│   └── eda.py                # Script for exploratory data analysis
│
├── /notebooks
│   ├── eda_fraud.ipynb       # Jupyter Notebook for fraud dataset analysis
│   └── eda_credit_card.ipynb  # Jupyter Notebook for credit card data analysis
│
└── README.md
```

## 1. Scripts

### preprocessing.py

This script contains functions for data preprocessing, including:

- **load_data**: Loads fraud and IP-to-country data from CSV files.
- **handle_missing_values**: Handles missing values in the dataset.
- **clean_data**: Removes duplicates and converts date columns to a standard format.
- **convert_ip_to_int**: Converts IP addresses from a float format to integers.
- **merge_ip_country**: Merges fraud data with country data using a range-based mechanism.
- **add_transaction_features**: Adds features related to transaction timing.
- **add_velocity_features**: Computes transaction velocity based on purchase times.
- **check_duplicated_ips**: Identifies duplicated IPs and summarizes their transaction data.
- **scale_features**: Scales numerical features for modeling.
- **encode_categorical**: Encodes categorical variables using one-hot encoding.
- **save_merged_data**: Saves the preprocessed data to a CSV file.

### eda.py

This script contains functions for exploratory data analysis, including:

- **univariate_analysis**: Visualizes the distribution of a single variable.
- **bivariate_analysis**: Visualizes the relationship between two variables.
- **plot_correlation_matrix**: Displays the correlation matrix of numerical features.
- **plot_top_fraud_countries**: Shows the top countries with fraud transactions.
- **transaction_recency_analysis**: Analyzes the time between signup and transaction in relation to fraud.
- **plot_class_distribution**: Visualizes the distribution of fraud and non-fraud classes.
- **plot_purchase_value_by_class**: Compares purchase values across fraud and non-fraud classes.
- **plot_age_distribution_by_class**: Shows the age distribution by fraud classes.
- **plot_transaction_time_diff_by_class**: Compares transaction time differences across classes.
- **plot_hour_class_relationship**: Analyzes transaction counts by hour of the day.
- **plot_day_class_relationship**: Analyzes transaction counts by day of the week.

## 2. Notebooks

### eda_fraud.ipynb

This Jupyter Notebook focuses on analyzing the fraud dataset. It includes:

1. **Importing Necessary Packages**: Sets the environment for the analysis.
2. **Loading Data**: Loads fraud and IP-to-country datasets.
3. **Data Overview**: Provides an overview and summary statistics of the datasets.
4. **Data Preprocessing**: Cleans and prepares the data for analysis.
5. **Feature Engineering**: Adds relevant features to the dataset.
6. **Exploratory Data Analysis (EDA)**: Analyzes various aspects of the dataset, including univariate and bivariate analyses, correlation, and geolocation analysis.
7. **Scaling and Encoding**: Scales numerical features and encodes categorical features for modeling.
8. **Saving Merged Data**: Saves the preprocessed and scaled data for future use.

### eda_credit_card.ipynb

This Jupyter Notebook focuses on analyzing credit card transaction data. It includes:

1. **Context**: Discusses the importance of fraud detection in credit card transactions.
2. **Loading the Dataset**: Loads the credit card transaction dataset.
3. **Class Distribution**: Analyzes the distribution of normal and fraudulent transactions.
4. **Transaction Amount Analysis**: Compares transaction amounts across classes.
5. **Transaction Timing Analysis**: Examines the timing of transactions in relation to fraud.
6. **Correlation Analysis**: Analyzes correlations between features in the dataset.

## How to Run

1. Ensure you have the necessary packages installed. You can install the required packages using:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
2. Navigate to the `notebooks` directory and open the Jupyter Notebooks in your preferred environment.
3. Run the cells sequentially to preprocess the data and perform analyses.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.
