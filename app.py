from flask import Flask
from app.routes import routes_bp

app = Flask(__name__)
app.register_blueprint(routes_bp, url_prefix="/api")

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
        ]
    }

if __name__=='__main__':
    app.run(debug=True, port=5000)