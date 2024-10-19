import pandas as pd
import numpy as np

def load_data():
    fraud_data = pd.read_csv('Fraud_Data.csv')
    ip_country_data = pd.read_csv('IpAddress_to_Country.csv')
    credit_data = pd.read_csv('creditcard.csv')
    return fraud_data, ip_country_data, credit_data

def handle_missing_values(df):
    df = df.dropna()  # Modify as needed, e.g., imputation strategies
    return df

def clean_data(df):
    df = df.drop_duplicates()
    df['signup_time'] = pd.to_datetime(df['signup_time'])
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])
    return df

def convert_ip_to_int(df):
    # Convert IPs to a comparable integer format by scaling and rounding
    df['ip_address'] = df['ip_address'].astype(str).apply(lambda x: int(float(x.split('.')[0])))
    return df

def merge_ip_country(fraud_data, ip_country_data):
    # Standardize IP conversion in ip_country_data
    ip_country_data['lower_bound_ip_address'] = ip_country_data['lower_bound_ip_address'].astype(int)
    ip_country_data['upper_bound_ip_address'] = ip_country_data['upper_bound_ip_address'].astype(int)
    
    # Merge based on IP ranges
    fraud_data['country'] = fraud_data.apply(lambda row: match_ip_to_country(row['ip_address'], ip_country_data), axis=1)
    return fraud_data

def match_ip_to_country(ip, ip_data):
    match = ip_data[(ip_data['lower_bound_ip_address'] <= ip) & (ip_data['upper_bound_ip_address'] >= ip)]
    if len(match) > 0:
        return match['country'].values[0]
    return 'Unknown'

def feature_engineering(df):
    # Transaction recency from signup time
    df['recency_from_signup'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds()
    
    # Transaction frequency and velocity (transactions per user within 24 hours)
    df['transaction_count'] = df.groupby('user_id')['purchase_time'].transform('count')
    
    # Velocity: Number of transactions in the last 24 hours for the user
    df = df.sort_values(by=['user_id', 'purchase_time'])
    df['transaction_velocity_24h'] = df.groupby('user_id')['purchase_time'].transform(
        lambda x: x.diff().dt.total_seconds().fillna(0).rolling(24*60*60).count()
    )
    
    # Time-based features
    df['hour_of_day'] = df['purchase_time'].dt.hour
    df['day_of_week'] = df['purchase_time'].dt.dayofweek
    return df

def normalize_scale(df, columns):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def encode_categorical(df):
    df = pd.get_dummies(df, columns=['browser', 'source', 'sex'], drop_first=True)
    return df
