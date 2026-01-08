from flask import Flask, jsonify
from app.routes import routes_bp
import json

app = Flask(__name__)
app.register_blueprint(routes_bp, url_prefix="/api")

# Load JSON data into application memory
with open("data/employees.json") as employee_data:
    app.config['EMPLOYEE_DATA'] = json.load(employee_data)

# App health check
@app.route("/")
def home():
    return {
        'message': 'API is running',
        'endpoints': [
            'GET /api/employee/<int:employee_id>',
            'POST /api/employee',
            'DELETE /api/employee/<int:employee_id>'
        ],
        'employees': app.config['EMPLOYEE_DATA']
    }

if __name__=='__main__':
    app.run(debug=True, port=5000)