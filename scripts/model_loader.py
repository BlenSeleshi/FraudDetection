import mlflow
import mlflow.pyfunc
from flask import current_app

MODEL_URI = "mlruns\591150408309061687\ebd5447925ec4635983607658761e717\artifacts\MLP Fraud\model.pkl"

def load_model():
    return mlflow.pyfunc.load_model(current_app.config['MODEL_URI'])
