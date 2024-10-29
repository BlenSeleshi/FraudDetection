import pandas as pd

def load_data(filepath):
    data = pd.read_csv(filepath)
    # Preprocess data (e.g., handling dates, extracting trends)
    data['signup_time'] = pd.to_datetime(data['signup_time'])
    data['purchase_time'] = pd.to_datetime(data['purchase_time'])
    return data
