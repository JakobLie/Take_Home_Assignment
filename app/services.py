from flask import current_app

# Use service layer to decouple data operations from api route
class EmployeeService:
    """ Handles employee data operations """

    def get_by_id(employee_id):
        """ GET employee by id """

        employee_data = current_app.config['EMPLOYEE_DATA']
        # Brute force check for id exists
        for employee in employee_data:
            if employee['id'] == employee_id:
                return employee
        # If not found, return None
        return None
        