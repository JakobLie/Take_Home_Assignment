from flask import Blueprint, jsonify, request
from app.services import EmployeeService

# Create blueprint
routes_bp = Blueprint('routes', __name__)

# ================================================================================
# =========================== Employees Routes ===================================
# ================================================================================

# Task 1: Get an object based on ID from a list of JSON object.
@routes_bp.route("/employee/<int:employee_id>", methods=['GET'])
def get_employee_by_id(employee_id):
    """ GET employee object by id """

    employee = EmployeeService.get_by_id(employee_id)
    if employee is not None:
        return jsonify(employee), 200
    return {"error": "Employee not found"}, 404

# Task 1: Add a new object.
@routes_bp.route("/employee", methods=['POST'])
def create_employee():
    """ CREATE new employee object """

    new_employee_data = request.get_json()
    employee = EmployeeService.create(new_employee_data)

    if employee is not None:
        return jsonify(employee), 200
    return {"error": "Employee could not be created"}, 500