from scripts.model_loader import load_model
import pandas as pd

model = load_model()

def make_prediction(record):
    prediction = model.predict(pd.DataFrame([record]))
    return prediction[0] > 0.5  # Binary prediction
