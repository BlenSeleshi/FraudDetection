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
    plt.figure(figsize=(12, 8))
    
    # Select only numerical columns
    numerical_df = df.select_dtypes(include=['number'])
    
    # Calculate the correlation matrix
    corr = numerical_df.corr()
    
    # Plot the heatmap
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', square=True, linewidths=0.5)
    plt.title('Correlation Matrix of Numerical Features')
    plt.show()
    
def plot_top_fraud_countries(df):
    # Filter for fraud transactions
    fraud_data = df[df['class'] == 1]
    
    # Count occurrences of each country in fraud transactions
    country_fraud_counts = fraud_data['country'].value_counts().head(10)
    
    # Create a bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=country_fraud_counts.values, y=country_fraud_counts.index, palette='viridis')
    plt.title('Top 10 Countries with Fraud Transactions')
    plt.xlabel('Number of Fraud Transactions')
    plt.ylabel('Country')
    plt.show()
    
def transaction_recency_analysis(df):
    # Analyze recency (time between signup and transaction) in relation to fraud
    plt.figure(figsize=(10,6))
    sns.histplot(data=df, x='transaction_time_diff(hours)', hue='class', bins=50)
    plt.title('Transaction Recency and Fraud')
    plt.show()
    
def plot_class_distribution(df):
    # Plot the distribution of fraud and non-fraud classes
    plt.figure(figsize=(6, 4))
    sns.countplot(x='class', data=df, palette='Set2')
    plt.title('Distribution of Fraud vs. Non-Fraud Classes')
    plt.xlabel('Class (0: Non-Fraud, 1: Fraud)')
    plt.ylabel('Count')
    plt.show()

def plot_purchase_value_by_class(df):
    # Boxplot to show the distribution of purchase values across fraud and non-fraud classes
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='class', y='purchase_value', data=df, palette='Set1')
    plt.title('Purchase Value by Fraud Class')
    plt.xlabel('Class (0: Non-Fraud, 1: Fraud)')
    plt.ylabel('Purchase Value')
    plt.yscale('log')  # Log scale for better visibility
    plt.show()

def plot_age_distribution_by_class(df):
    # Plot age distribution by fraud and non-fraud classes
    plt.figure(figsize=(8, 6))
    sns.histplot(data=df, x='age', hue='class', multiple='stack', palette='Set1', bins=30)
    plt.title('Age Distribution by Fraud Class')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.show()

def plot_transaction_time_diff_by_class(df):
    # Boxplot to show transaction time differences across fraud and non-fraud classes
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='class', y='transaction_time_diff(hours)', data=df, palette='Set3')
    plt.title('Transaction Time Difference by Fraud Class')
    plt.xlabel('Class (0: Non-Fraud, 1: Fraud)')
    plt.ylabel('Time Difference (hours)')
    plt.yscale('log')  # Log scale for better visibility
    plt.show()

def plot_hour_class_relationship(df):
    plt.figure(figsize=(12, 6))
    
    # Count of each class for each hour of the day
    hour_class_count = df.groupby(['hour_of_day', 'class']).size().unstack(fill_value=0)
    
    # Plotting
    hour_class_count.plot(kind='bar', stacked=True, color=['lightblue', 'salmon'], edgecolor='black')
    plt.title('Count of Fraud and Non-Fraud Transactions by Hour of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Count of Transactions')
    plt.xticks(rotation=0)
    plt.legend(title='Class', labels=['Non-Fraud (0)', 'Fraud (1)'])
    plt.grid(axis='y', linestyle='--')
    plt.show()

def plot_day_class_relationship(df):
    plt.figure(figsize=(12, 6))
    
    # Count of each class for each day of the week
    day_class_count = df.groupby(['day_of_week', 'class']).size().unstack(fill_value=0)
    
    # Plotting
    day_class_count.plot(kind='bar', stacked=True, color=['lightblue', 'salmon'], edgecolor='black')
    plt.title('Count of Fraud and Non-Fraud Transactions by Day of Week')
    plt.xlabel('Day of the Week (0=Monday, 6=Sunday)')
    plt.ylabel('Count of Transactions')
    plt.xticks(rotation=0)
    plt.legend(title='Class', labels=['Non-Fraud (0)', 'Fraud (1)'])
    plt.grid(axis='y', linestyle='--')
    plt.show()
