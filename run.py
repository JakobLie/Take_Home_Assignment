from flask import Flask, jsonify, request
from app.routes import routes_bp
import json
import logging

app = Flask(__name__)
app.register_blueprint(routes_bp, url_prefix="/api")

# Task 2: Log down all requests to the backend.
# Configure logging at INFO level
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        # Log to file "app.log" and to console
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Additionally, log payloads of requests
@app.before_request
def log_request():
    if request.data:
        logger.info(f"Incoming {request.method} with Request Body: {request.get_json()}")

# Load JSON data into application memory
with open("data/employees.json") as employee_data:
    app.config['EMPLOYEE_DATA'] = json.load(employee_data)

# App health check
@app.route("/")
def home():
    return {
        'message': 'App is running',
        'endpoints': [
            'GET /api/employee/<int:employee_id>',
            'POST /api/employee',
            'DELETE /api/employee/<int:employee_id>'
        ],
        'employees': app.config['EMPLOYEE_DATA']
    }

if __name__=='__main__':
    app.run(debug=True, port=5000)