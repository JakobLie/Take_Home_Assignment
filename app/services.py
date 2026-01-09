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

        employee_data = current_app.config['EMPLOYEE_DATA']

        # Task 3: Validation
        # Check that payload exists
        if not payload:
            return None, ({"error": "No data provided"}, 400)

        # Check that all required fields are present and not null
        required_fields = ['name', 'email', 'phone'] # id is AUTO INCREMENTED to prevent duplication
        for field in required_fields:
            if field not in payload:
                return None, ({"error": f"Missing required field '{field}'"}, 422)
            if payload[field].strip() is None or payload[field].strip()=="":
                return None, ({"error": f"Field '{field}' cannot be empty"}, 422)
            
        # Check that unique details (email, phone) are not already in data
        for employee in employee_data:
            if employee['email'].lower().strip()==payload['email'].lower().strip():
                return None, ({"error": "Cannot create employee object with duplicate email"}, 422)
            if employee['phone'].strip()==payload['phone'].strip():
                return None, ({"error": "Cannot create employee object with duplicate phone number"}, 422)

        # If all checks pass, attempt to add employee
        employee_data = current_app.config['EMPLOYEE_DATA']

        new_employee = {
            "id": employee_data[-1]['id']+1 if employee_data else 1, # if no employees set to 1 else AUTO_INCREMENT
            "name": payload['name'],
            "email": payload['email'],
            "phone": payload['phone']
        }

        try:
            employee_data.append(new_employee)
            return new_employee, None
        except Exception as e:
            return None, ({"error": f"Failed to create employee object:{str(e)}"}, 500)
        
    def delete_by_id(employee_id):
        """ DELETE employee object by id """

        employee_data = current_app.config['EMPLOYEE_DATA']

        # Task 3: Validation

        for employee in employee_data:
            if employee['id'] == employee_id:
                try:
                    employee_data.remove(employee)
                    return employee, None
                except Exception as e:
                    return None, ({"error": f"Failed to delete employee object: {str(e)}"}, 500)
        # If not found, return None
        return None, ({"error": f"Employee with id {employee_id} does not exist"}, 404)