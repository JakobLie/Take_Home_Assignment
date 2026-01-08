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
            'GET /api/<tbc>',
            'POST /api/<tbc>',
            'PUT /api/<tbc>',
            'DELETE /api/<tbc>'
        ],
        'employees': app.config['EMPLOYEE_DATA']
    }

if __name__=='__main__':
    app.run(debug=True, port=5000)