
import sys 
import os 
 
# Add root directory to the system path so that "app" module can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from unittest.mock import patch
from flask import Flask
from app.routes import routes_bp

class TestEmployeeRoutes(unittest.TestCase):
    def setUp(self):
        # Create flask app
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True

        # Register the blueprint
        self.app.register_blueprint(routes_bp, url_prefix="/api")

        # Initialize test client
        self.client = self.app.test_client()

    # ==============================================================================
    # ============================= GET UNIT TESTS =================================
    # ==============================================================================

    @patch('app.routes.EmployeeService.get_by_id')
    def test_get_employee_by_id_success(self, mock_get_by_id):
        """ Test GET /api/employee/<id> returns employee object successfully """

        # Mock the service response
        mock_employee = {
            "email": "alice.tan@gmail.com",
            "id": 1,
            "name": "Alice Tan",
            "phone": "+65 9123 4567"
        }
        mock_get_by_id.return_value = (mock_employee, None)

        # Call the route
        response = self.client.get("/api/employee/1")
        data = response.get_json()

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "Alice Tan")
        self.assertEqual(data["email"], "alice.tan@gmail.com")
        self.assertEqual(data["phone"], "+65 9123 4567")

        # Verify mock service method called with id 1
        mock_get_by_id.assert_called_once_with(1)

    @patch('app.routes.EmployeeService.get_by_id')
    def test_get_employee_by_id_not_found(self, mock_get_by_id):
        """ Test GET /api/employee/<id> returns employee not found """

        # Mock the service response
        mock_error = ({"error": "Employee with id 100 not found"}, 404)
        mock_get_by_id.return_value = (None, mock_error)

        # Call the route
        response = self.client.get("/api/employee/100")
        data = response.get_json()

        # Assertions
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["error"], "Employee with id 100 not found")

        # Verify mock service method called with id 100
        mock_get_by_id.assert_called_once_with(100)

    # ==============================================================================
    # ============================ POST UNIT TESTS =================================
    # ==============================================================================

    @patch('app.routes.EmployeeService.create')
    def test_create_employee_success(self, mock_create):
        """ Test POST /api/employee returns employee object successfully """

        # Mock the service response
        mock_employee = {
            "id": 6, # Since json data contains 5 employee objects, and id should AUTO_INCREMENT
            "name": "Jason Liew",
            "email": "jason.liew@gmail.com",
            "phone": "+65 9512 8122"
        }
        mock_create.return_value = (mock_employee, None)

        payload = {
            "name": "Jason Liew",
            "email": "jason.liew@gmail.com",
            "phone": "+65 9512 8122"
        }

        # Call the route
        response = self.client.post("/api/employee", json=payload)
        data = response.get_json()

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], 6)
        self.assertEqual(data["name"], "Jason Liew")
        self.assertEqual(data["email"], "jason.liew@gmail.com")
        self.assertEqual(data["phone"], "+65 9512 8122")

        # Verify mock service method called with payload data
        mock_create.assert_called_once_with(payload)

    @patch('app.routes.EmployeeService.create')
    def test_create_employee_empty_payload(self, mock_create):
        """ Test POST /api/employee returns no data error """

        # Mock the service response
        mock_error = ({"error": "No data provided"}, 400)
        mock_create.return_value = (None, mock_error)

        payload = {}

        # Call the route
        response = self.client.post("/api/employee", json=payload)
        data = response.get_json()

        # Assertions
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "No data provided")

        # Verify mock service method called with payload data
        mock_create.assert_called_once_with(payload)
    
    @patch('app.routes.EmployeeService.create')
    def test_create_employee_missing_fields(self, mock_create):
        """ Test POST /api/employee returns mising fields error """

        # Mock the service response
        mock_error = ({"error": f"Missing required field 'email'"}, 422)
        mock_create.return_value = (None, mock_error)

        payload = {
            "name": "Jason Liew",
            # "email": "jason.liew@gmail.com", # Remove required field 'email'
            "phone": "+65 9512 8122"
        }

        # Call the route
        response = self.client.post("/api/employee", json=payload)
        data = response.get_json()

        # Assertions
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data["error"], "Missing required field 'email'")

        # Verify mock service method called with payload data
        mock_create.assert_called_once_with(payload)
    
    @patch('app.routes.EmployeeService.create')
    def test_create_employee_empty_fields(self, mock_create):
        """ Test POST /api/employee returns empty field error """

        # Mock the service response
        mock_error = ({"error": "Field 'name' cannot be empty"}, 422)
        mock_create.return_value = (None, mock_error)

        payload = {
            "name": "", # Set name to empty string
            "email": "jason.liew@gmail.com",
            "phone": "+65 9512 8122"
        }

        # Call the route
        response = self.client.post("/api/employee", json=payload)
        data = response.get_json()

        # Assertions
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data["error"], "Field 'name' cannot be empty")

        # Verify mock service method called with payload data
        mock_create.assert_called_once_with(payload)


    # ==============================================================================
    # =========================== DELETE UNIT TESTS ================================
    # ==============================================================================

    @patch('app.routes.EmployeeService.delete_by_id')
    def test_delete_employee_by_id_success(self, mock_delete):
        """ Test DELETE /api/employee/<id> returns employee deleted successfully """

        # Mock the service response
        mock_employee = {
            "id": 6,
            "name": "Jason Liew",
            "email": "jason.liew@gmail.com",
            "phone": "+65 9512 8122"
        }
        mock_delete.return_value = (None, mock_employee)

        # Call the route
        response = self.client.delete("/api/employee/6")
        data = response.get_json()

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], 6)
        self.assertEqual(data["name"], "Jason Liew")
        self.assertEqual(data["email"], "jason.liew@gmail.com")
        self.assertEqual(data["phone"], "+65 9512 8122")

        # Verify mock service method called with payload data
        mock_delete.assert_called_once_with(6)
    
    @patch('app.routes.EmployeeService.delete_by_id')
    def test_delete_employee_by_id_failure(self, mock_delete):
        """ Test DELETE /api/employee/<id> returns failed to delete error """

        # Mock the service response
        mock_error = ({"error": "Employee with id 100 does not exist"}, 404)
        mock_delete.return_value = (None, mock_error)

        # Call the route
        response = self.client.delete("/api/employee/100")
        data = response.get_json()

        # Assertions
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["error"], "Employee with id 100 does not exist")

        # Verify mock service method called with payload data
        mock_delete.assert_called_once_with(100)


if __name__ == "__main__":
    unittest.main()