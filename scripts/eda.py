import matplotlib.pyplot as plt
import seaborn as sns

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

def fraud_by_country_analysis(df):
    # Analyze fraud frequency by country
    fraud_per_country = df.groupby('country')['class'].mean().sort_values(ascending=False)
    plt.figure(figsize=(12,6))
    fraud_per_country.plot(kind='bar', color='salmon')
    plt.title('Fraud Frequency by Country')
    plt.show()

def transaction_velocity_analysis(df):
    # Analyze how transaction velocity relates to fraud
    plt.figure(figsize=(10,6))
    sns.histplot(data=df, x='transaction_velocity', hue='class', bins=50)
    plt.title('Transaction Velocity and Fraud')
    plt.show()

def transaction_recency_analysis(df):
    # Analyze recency (time between signup and transaction) in relation to fraud
    plt.figure(figsize=(10,6))
    sns.histplot(data=df, x='transaction_time_diff', hue='class', bins=50)
    plt.title('Transaction Recency and Fraud')
    plt.show()
