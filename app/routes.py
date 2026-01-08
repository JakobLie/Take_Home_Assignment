from flask import Blueprint, jsonify
from app.services import EmployeeService

# Create blueprint
routes_bp = Blueprint('routes', __name__)

# ================================================================================
# =========================== Employees Routes ===================================
# ================================================================================

# Task 1: Get an object based on ID from a list of JSON object.
@routes_bp.route("/employee/<int:employee_id>", methods=['GET'])
def get_employee_by_id(employee_id):
    """ GET employee by id """
    employee = EmployeeService.get_by_id(employee_id)
    if employee is not None:
        return jsonify(employee)
    return {"error": "Employee not found"}, 404