import mlflow
import mlflow.pyfunc
from flask import current_app

MODEL_URI = r"C:/Users/Blen/OneDrive/Desktop/10Academy/FraudDetection/mlruns/591150408309061687/ebd5447925ec4635983607658761e717/artifacts/MLP Fraud"

def load_model():
    return mlflow.sklearn.load_model(MODEL_URI)
