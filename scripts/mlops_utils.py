import mlflow
import mlflow.sklearn
from sklearn.metrics import accuracy_score, precision_score, f1_score, roc_auc_score, confusion_matrix

def start_mlflow_experiment(experiment_name):
    mlflow.set_experiment(experiment_name)
    mlflow.start_run()

def log_metrics(metrics_dict):
    for metric, value in metrics_dict.items():
        mlflow.log_metric(metric, value)

def log_model(model, model_name):
    mlflow.sklearn.log_model(model, model_name)

def end_mlflow_run():
    mlflow.end_run()

# Example usage in training
def log_experiment_results(model_name, y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred)
    
    metrics_dict = {
        'accuracy': accuracy,
        'precision': precision,
        'f1_score': f1,
        'roc_auc': roc_auc
    }
    
    start_mlflow_experiment(model_name)
    log_metrics(metrics_dict)
    log_model(model_name, model_name)
    end_mlflow_run()
