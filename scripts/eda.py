import matplotlib.pyplot as plt
import seaborn as sns

def fraud_rate_by_country(df):
    fraud_rate = df.groupby('country')['class'].mean().sort_values(ascending=False)
    plt.figure(figsize=(12,6))
    fraud_rate.plot(kind='bar', color='red')
    plt.title('Fraud Rate by Country')
    plt.show()

def transaction_count_by_country(df):
    transaction_count = df['country'].value_counts().sort_values(ascending=False)
    plt.figure(figsize=(12,6))
    transaction_count.plot(kind='bar', color='green')
    plt.title('Transaction Count by Country')
    plt.show()

def univariate_analysis(df, column):
    plt.figure(figsize=(10,6))
    sns.histplot(df[column], kde=True)
    plt.title(f'Univariate Analysis of {column}')
    plt.show()

def bivariate_analysis(df, column1, column2):
    plt.figure(figsize=(10,6))
    sns.scatterplot(x=column1, y=column2, data=df, hue='class')
    plt.title(f'Bivariate Analysis of {column1} and {column2}')
    plt.show()

def plot_correlation_matrix(df):
    plt.figure(figsize=(12,8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

def transaction_value_analysis(df):
    plt.figure(figsize=(10,6))
    sns.boxplot(x='class', y='purchase_value', data=df)
    plt.title('Transaction Value Distribution by Fraud Status')
    plt.show()

def time_of_day_analysis(df):
    plt.figure(figsize=(10,6))
    sns.histplot(df['hour_of_day'], bins=24, hue='class', multiple='stack')
    plt.title('Fraud Occurrences by Time of Day')
    plt.show()
