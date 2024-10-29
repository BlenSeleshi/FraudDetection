import logging
from flask import request

def setup_logging(app):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("fraud_detection")

    @app.before_request
    def log_request_info():
        logger.info(f"Received request: {request.method} {request.path}")
        if request.data:
            logger.info(f"Request data: {request.data}")

    @app.after_request
    def log_response_info(response):
        logger.info(f"Response status: {response.status}")
        return response
