from flask import current_app

# Use service layer to decouple data operations from api route
class EmployeeService:
    """ Handles employee data operations """

    def get_by_id(employee_id):
        """ GET employee object by id """

        employee_data = current_app.config['EMPLOYEE_DATA']
        # Check for employee id
        for employee in employee_data:
            if employee['id'] == employee_id:
                return employee, None
        # If not found, return None
        return None, ({"error": f"Employee with id {employee_id} not found"}, 404)
        
    def create(payload):
        """ CREATE new employee object """

        new_employee = {
            "id": payload['id'],
            "name": payload['name'],
            "email": payload['email'],
            "phone": payload['phone']
        }

        employee_data = current_app.config['EMPLOYEE_DATA']

        try:
            employee_data.append(new_employee)
            return new_employee, None
        except:
            return None, ({"error": "Failed to create employee object"}, 500)
        
    def delete_by_id(employee_id):
        """ DELETE employee object by id """

        employee_data = current_app.config['EMPLOYEE_DATA']

        for employee in employee_data:
            if employee['id'] == employee_id:
                try:
                    employee_data.remove(employee)
                    return employee, None
                except:
                    return None, ({"error": "Failed to create new employee object"}, 500)
        # If not found, return None
        return None, ({"error": f"Employee with id {employee_id} does not exist"}, 404)