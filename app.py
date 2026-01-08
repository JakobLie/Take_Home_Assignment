from flask import Flask
app = Flask(__name__)

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