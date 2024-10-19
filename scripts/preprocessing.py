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
    # Convert IPs in the country dataset to int format
    ip_country_data['lower_bound_ip_address'] = ip_country_data['lower_bound_ip_address'].astype(int)
    ip_country_data['upper_bound_ip_address'] = ip_country_data['upper_bound_ip_address'].astype(int)

    # Merge by finding where IP falls within the bounds
    fraud_data = fraud_data.merge(ip_country_data, how='left',
                                  left_on='ip_address',
                                  right_on='lower_bound_ip_address')
    return fraud_data

def add_transaction_features(df):
    # Time between signup and purchase (recency feature)
    df['transaction_time_diff'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds()

    # Hour and Day of purchase
    df['hour_of_day'] = df['purchase_time'].dt.hour
    df['day_of_week'] = df['purchase_time'].dt.dayofweek
    
    return df

def add_velocity_features(df):
    # Transaction velocity: Count transactions within the last X hours
    df = df.sort_values(by='purchase_time')
    df['transaction_velocity'] = df.groupby('user_id')['purchase_time'].diff().dt.total_seconds().fillna(0)
    return df

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
