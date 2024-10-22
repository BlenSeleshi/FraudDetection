import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_data(filepath1, filepath2):
    fraud_data = pd.read_csv(filepath1)
    ip_country_data = pd.read_csv(filepath2)
    #credit_data = pd.read_csv(filepath3)
    return fraud_data, ip_country_data

def handle_missing_values(df):
    df = df.dropna()
    return df

def clean_data(df):
    # Remove duplicates and correct data types
    df = df.drop_duplicates()
    df['signup_time'] = pd.to_datetime(df['signup_time'])
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])
    return df

def convert_ip_to_int(df):
    # Handle IP addresses with decimal points (Fraud_Data.csv format)
    df['ip_address'] = df['ip_address'].astype(float).apply(np.floor).astype(int)
    return df

def merge_ip_country(fraud_data, ip_country_data):
    # Convert IP columns to int64 for both fraud_data and ip_country_data
    fraud_data['ip_address'] = fraud_data['ip_address'].astype(int)
    ip_country_data['lower_bound_ip_address'] = ip_country_data['lower_bound_ip_address'].astype(int)
    ip_country_data['upper_bound_ip_address'] = ip_country_data['upper_bound_ip_address'].astype(int)

    # Sort the ip_country_data by 'lower_bound_ip_address'
    ip_country_data = ip_country_data.sort_values(by='lower_bound_ip_address')

    # Perform the range-based merge using merge_asof
    fraud_data = pd.merge_asof(fraud_data.sort_values('ip_address'), 
                               ip_country_data[['lower_bound_ip_address', 'upper_bound_ip_address', 'country']],
                               left_on='ip_address', 
                               right_on='lower_bound_ip_address',
                               direction='backward')

    # Filter to retain only rows where the ip_address falls within the valid IP range
    fraud_data = fraud_data[(fraud_data['ip_address'] >= fraud_data['lower_bound_ip_address']) & 
                            (fraud_data['ip_address'] <= fraud_data['upper_bound_ip_address'])]

    return fraud_data


def add_transaction_features(df):
    # Time between signup and purchase (recency feature)
    df['transaction_time_diff(hours)'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds() / 3600

    # Hour and Day of purchase
    df['hour_of_day'] = df['purchase_time'].dt.hour
    df['day_of_week'] = df['purchase_time'].dt.dayofweek
    df['month_of_year'] = df['purchase_time'].dt.month
    
    return df

def add_velocity_features(df):
    # Transaction velocity: Count transactions within the last X hours
    df = df.sort_values(by='purchase_time')
    df['transaction_velocity'] = df.groupby('ip_address')['purchase_time'].diff().dt.total_seconds().fillna(0)
    return df

def check_duplicated_ips(df):
    # Group by IP address to find duplicated IPs
    duplicated_ips = df.groupby('ip_address').agg(
        total_purchase_amount=('purchase_value', 'sum'),
        purchase_count=('purchase_value', 'size'),
        country=('country', 'first'),  # Assuming you've already merged the country info
        fraud_class=('class', 'first')  # Assuming fraud class is consistent for same IPs
    ).reset_index()
    
    # Filter for IPs that have more than 1 purchase (i.e., duplicated IPs)
    duplicated_ips = duplicated_ips[duplicated_ips['purchase_count'] > 1]
    
    return duplicated_ips


def scale_features(df, columns):
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def encode_categorical(df):
    # One-hot encode categorical features
    df = pd.get_dummies(df, columns=['browser', 'source', 'sex'], drop_first=True)
    return df

def save_merged_data(df, filename='merged_fraud_data.csv'):
    df.to_csv(filename, index=False)
