# README for Fraud Detection Project

## Project Overview

This project focuses on detecting fraudulent transactions in e-commerce and credit card data. It involves data preprocessing, exploratory data analysis (EDA), feature engineering, and model training to enhance fraud detection capabilities.

## Directory Structure

```
/fraud_detection_project
│
├── /scripts
│   ├── preprocessing.py      # Functions for data preprocessing and feature engineering
│   └── eda.py                # Functions for exploratory data analysis
│
├── /notebooks
│   ├── eda_fraud.ipynb       # Jupyter Notebook for fraud dataset analysis
│   └── eda_credit_card.ipynb  # Jupyter Notebook for credit card data analysis
│
└── README.md
```

## Key Components

### Scripts

- **preprocessing.py**: Contains functions for:

  - Loading and cleaning datasets
  - Converting IP addresses to integer format
  - Merging datasets based on geographical information
  - Adding transaction-related features and handling missing values
  - Scaling numerical features and encoding categorical variables
  - Saving the processed data for further analysis

- **eda.py**: Includes functions for:
  - Performing univariate and bivariate analysis
  - Visualizing class distributions and correlations
  - Analyzing geographical patterns in fraudulent transactions

### Notebooks

- **eda_fraud.ipynb**:

  - Analyzes the fraud dataset with steps for loading data, preprocessing, feature engineering, and conducting EDA.
  - Explores transaction features, visualizes distributions, and examines relationships between variables.

- **eda_credit_card.ipynb**:
  - Focuses on credit card transaction data analysis.
  - Examines transaction class distribution, amounts, timing, and correlations.

## How to Run

1. Install the required packages:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
2. Open the Jupyter Notebooks in your preferred environment and run the cells sequentially for data analysis.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or new features.
