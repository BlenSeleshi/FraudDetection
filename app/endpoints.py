from flask import jsonify, request
from predictions import make_prediction

def setup_endpoints(app, data):

    @app.route('/api/summary', methods=['GET'])
    def get_summary():
        summary = {
            "total_transactions": len(data),
            "total_fraud_cases": data['class'].sum(),
            "fraud_percentage": (data['class'].sum() / len(data)) * 100
        }
        return jsonify(summary)

    @app.route('/api/predict', methods=['POST'])
    def predict():
        record = request.json
        prediction = make_prediction(record)
        return jsonify({"prediction": int(prediction)})
