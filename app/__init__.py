from flask import Flask
from .logging_config import setup_logging
from .endpoints import setup_endpoints
from .data_loader import load_data
from dashboard import create_dashboard

app = Flask(__name__)
setup_logging(app)  # Initialize logging

# Load data and register endpoints
data = load_data(r'C:\Users\Blen\OneDrive\Desktop\10Academy\CreditScoreModeling\data\data.csv')
setup_endpoints(app, data)

# Initialize and integrate Dash into Flask
app = create_dashboard(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
