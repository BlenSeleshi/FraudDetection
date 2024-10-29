# fraud_detection_dashboard/app/main.py
from flask import Flask
from .data_loader import load_data
from .endpoints import setup_endpoints
from .logging_config import setup_logging
from dashboard import create_dashboard

# Initialize Flask app
app = Flask(__name__)

# Setup logging
setup_logging(app)

# Load data and assign it to a global variable
data = load_data('data/fraud_data.csv')

# Register Flask API endpoints with data
setup_endpoints(app, data)

# Initialize Dash and attach it to the Flask app
app = create_dashboard(app, data)  # Pass data to the Dash app

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
