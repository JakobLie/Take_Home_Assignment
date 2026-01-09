# Integrated testing of service logic with temp testing app

import sys 
import os 
 
# Add root directory to the system path so that "app" module can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from flask import Flask
from app.services import EmployeeService

class TestEmployeeServices(unittest.TestCase):
    
    def setUp(self):
        """Set up flask app before each test """
        
        self.app = Flask(__name__)

        # Add all employee employee
        self.app.config['EMPLOYEE_DATA'] = [
            {
                "id": 1,
                "name": "Alice Tan",
                "email": "alice.tan@gmail.com",
                "phone": "+65 9123 4567"
            },
            {
                "id": 2,
                "name": "Ben Lim",
                "email": "ben.lim@gmail.com",
                "phone": "+65 9234 5678"
            },
            {
                "id": 3,
                "name": "Cheryl Ng",
                "email": "cheryl.ng@gmail.com",
                "phone": "+65 9345 6789"
            },
            {
                "id": 4,
                "name": "Daniel Koh",
                "email": "daniel.koh@gmail.com",
                "phone": "+65 9456 7890"
            },
            {
                "id": 5,
                "name": "Emily Goh",
                "email": "emily.goh@gmail.com",
                "phone": "+65 9567 8901"
            }
        ]

        # Create and push app context
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """ Clean up app after each test """
        self.app_context.pop()

    # ==============================================================================
    # ======================== GET INTEGRATION TESTS ===============================
    # ==============================================================================

    def test_get_employeea_by_id_success(self):
        """ Test GET /api/employee/<id> returns employee object successfully """

        # Call the route
        employee, error = EmployeeService.get_by_id(1)

        # Assertions
        self.assertIsNone(error)
        self.assertIsNotNone(employee)
        self.assertEqual(employee["id"], 1)
        self.assertEqual(employee["name"], "Alice Tan")
        self.assertEqual(employee["email"], "alice.tan@gmail.com")
        self.assertEqual(employee["phone"], "+65 9123 4567")

    def test_get_employee_by_id_not_found(self):
        """ Test GET employee by non-existent ID returns not found error """

        # Call the route
        employee, error = EmployeeService.get_by_id(100)
        
        # Assertions
        self.assertIsNone(employee)
        self.assertIsNotNone(error)
        self.assertEqual(error[1], 404)
        self.assertIn("not found", error[0]["error"].lower())

    # ==============================================================================
    # ======================= CREATE INTEGRATION TESTS =============================
    # ==============================================================================

    def test_create_employee_success(self):
        """ Test POST /api/employee returns employee object successfully """

        payload = {
            "name": "Jason Liew",
            "email": "jason.liew@gmail.com",
            "phone": "+65 9512 8122"
        }

        # Call the route
        employee, error = EmployeeService.create(payload)

        # Assertions
        self.assertIsNone(error)
        self.assertIsNotNone(employee)
        self.assertEqual(employee["id"], 6)  # Since  data has 5 employee objects, and id should AUTO_INCREMENT
        self.assertEqual(employee["name"], "Jason Liew")
        self.assertEqual(employee["email"], "jason.liew@gmail.com")
        self.assertEqual(employee["phone"], "+65 9512 8122")
    
    def test_create_employee_empty_payload(self):
        """ Test POST /api/employee returns no data error """

        payload = {}

        # Call the route
        employee, error = EmployeeService.create(payload)

        # Assertions
        self.assertIsNone(employee)
        self.assertIsNotNone(error)
        self.assertEqual(error[0]["error"], "No data provided")
        self.assertEqual(error[1], 400)

    def test_create_employee_missing_fields(self):
        """ Test POST /api/employee returns missing fields error """

        payload = {
            "name": "Jason Liew",
            # "email": "jason.liew@gmail.com", # Remove required field 'email'
            "phone": "+65 9512 8122"
        }

        # Call the route
        employee, error = EmployeeService.create(payload)

        # Assertions
        self.assertIsNone(employee)
        self.assertIsNotNone(error)
        self.assertEqual(error[0]["error"], "Missing required field 'email'")
        self.assertEqual(error[1], 422)
    
    def test_create_employee_empty_fields(self):
        """ Test POST /api/employee returns empty field error """

        payload = {
            "name": "", # Set name to empty string
            "email": "jason.liew@gmail.com",
            "phone": "+65 9512 8122"
        }

        # Call the route
        employee, error = EmployeeService.create(payload)

        # Assertions
        self.assertIsNone(employee)
        self.assertIsNotNone(error)
        self.assertEqual(error[0]["error"], "Field 'name' cannot be empty")
        self.assertEqual(error[1], 422)
    
    # ==============================================================================
    # ======================= DELETE INTEGRATION TESTS =============================
    # ==============================================================================
    
    def test_delete_employee_by_id_success(self):
        """ Test DELETE /api/employee/<id> returns employee deleted successfully """

        # Call the route
        employee, error = EmployeeService.delete_by_id(1)

        # Assertions
        self.assertIsNone(error)
        self.assertIsNotNone(employee)
        self.assertEqual(employee["id"], 1)
        self.assertEqual(employee["name"], "Alice Tan")
        self.assertEqual(employee["email"], "alice.tan@gmail.com")
        self.assertEqual(employee["phone"], "+65 9123 4567")

    def test_delete_employee_by_id_not_found(self):
        """ Test DELETE /api/employee/<id> returns not found error """

        # Call the route
        employee, error = EmployeeService.delete_by_id(100)

        # Assertions
        self.assertIsNone(employee)
        self.assertIsNotNone(error)
        self.assertEqual(error[0]["error"], "Employee with id 100 does not exist")
        self.assertEqual(error[1], 404)

if __name__ == "__main__":
    unittest.main()