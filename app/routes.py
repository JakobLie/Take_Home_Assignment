from flask import Blueprint

# Create blueprint
routes_bp = Blueprint('routes', __name__)

@routes_bp.route("/test")
def home():
    return "BP works"