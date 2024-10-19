# Fraud Detection Project

## Overview

This project focuses on building a fraud detection system using machine learning techniques to analyze and identify fraudulent transactions in e-commerce and banking contexts. The scripts in this repository include data preprocessing and exploratory data analysis (EDA) functionalities.

## Directory Structure

```
/project-directory
│
├── scripts/
│   ├── preprocessing.py
│   └── eda.py
│
└── data/
    ├── Fraud_Data.csv
    ├── IpAddress_to_Country.csv
    └── creditcard.csv
```

## Requirements

To run the scripts, ensure you have the following Python libraries installed:

- `pandas`
- `numpy`
- `sklearn`
- `matplotlib`
- `seaborn`

You can install the required libraries using pip:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

## Usage

### Preprocessing Script: `preprocessing.py`

This script handles data loading, cleaning, feature engineering, and preparation for modeling. It performs the following steps:

1. **Load Data**: Reads the necessary CSV files.
2. **Handle Missing Values**: Removes rows with missing values.
3. **Clean Data**: Removes duplicates and converts timestamps to datetime objects.
4. **Convert IP Addresses**: Transforms IP addresses from decimal format to integer format.
5. **Merge IP and Country Data**: Merges fraud data with country information based on IP address ranges.
6. **Add Transaction Features**: Creates features related to transaction timing and frequency.
7. **Add Velocity Features**: Computes transaction velocity based on time differences.
8. **Check Duplicated IPs**: Identifies IPs with multiple transactions.
9. **Scale Features**: Standardizes specified numerical features.
10. **Encode Categorical Features**: Applies one-hot encoding to categorical variables.
11. **Save Merged Data**: Exports the cleaned and merged DataFrame to a CSV file.

#### Example Usage

```python
import preprocessing as pp

# Load the data
fraud_data, ip_country_data = pp.load_data('data/Fraud_Data.csv', 'data/IpAddress_to_Country.csv')

# Clean and preprocess the data
cleaned_data = pp.clean_data(fraud_data)
merged_data = pp.merge_ip_country(cleaned_data, ip_country_data)
final_data = pp.add_transaction_features(merged_data)

# Save the processed data
pp.save_merged_data(final_data)
```

### EDA Script: `eda.py`

This script is designed for exploratory data analysis to visualize and understand the relationships and distributions in the dataset. It includes the following functionalities:

1. **Univariate Analysis**: Analyzes the distribution of a single feature.
2. **Bivariate Analysis**: Explores the relationship between two features.
3. **Correlation Matrix**: Visualizes correlations among numerical features.
4. **Fraud by Country**: Plots the top countries with fraudulent transactions.
5. **Transaction Recency Analysis**: Examines the time between signup and purchase in relation to fraud.
6. **Class Distribution**: Displays the distribution of fraud and non-fraud classes.
7. **Purchase Value Analysis**: Analyzes purchase values across fraud classes.
8. **Age Distribution by Class**: Shows age distributions segmented by fraud classification.
9. **Transaction Time Difference Analysis**: Compares transaction time differences across classes.
10. **Hourly and Daily Class Relationships**: Analyzes transactions by hour of the day and day of the week.

#### Example Usage

```python
import pandas as pd
import eda as eda

# Load the processed data
data = pd.read_csv('merged_fraud_data.csv')

# Perform EDA
eda.plot_class_distribution(data)
eda.plot_top_fraud_countries(data)
eda.transaction_recency_analysis(data)
```

## Conclusion

The provided scripts serve as the foundation for building a robust fraud detection model. Users can extend the preprocessing and EDA functionalities to suit their specific requirements as needed.
