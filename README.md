# Employee Management API

A RESTful API built with Flask for managing employee records with CRUD operations, request logging, validation, and dependency injection.

## Live Demo

**Deployed URL:** [https://take-home-assignment-8f4o2mjtw-jakobs-projects-815d80ba.vercel.app/](https://take-home-assignment-8f4o2mjtw-jakobs-projects-815d80ba.vercel.app/)

## Features

- RESTful API with GET, POST, DELETE endpoints
- Request logging with timestamps and payloads
- Validation for create/delete operations
- Dependency injection with service layer pattern
- Unit & integration tests with mocking

## API Endpoints

### Get Employee by ID
```http
GET /api/employee/{id}
```

### Create Employee
```http
POST /api/employee
Content-Type: application/json

{
  "name": "Jason Liew",
  "email": "jason.liew@gmail.com",
  "phone": "+65 9512 8122"
}
```

### Delete Employee
```http
DELETE /api/employee/{id}
```

## Postman Collection

Import the included `postman_collection.json` file to test all endpoints locally.

## Running Tests

```bash
# Unit tests (with mocking)
python tests/unit_tests.py

# Integration tests
python tests/integration_tests.py

# All tests
python -m unittest discover tests
```

## Task Completion

- **Task 1:** Backend API with 3 endpoints (GET, POST, DELETE)
- **Task 2:** Request logging
- **Task 3:** Request validation
- **Task 4:** Unit test cases
- **Task 5:** Dependency injection (EmployeeService)

## Validation Rules

**Required Fields:** `name`, `email`, `phone` (all non-empty)

**Business Rules:**
- Auto-incrementing IDs
- Unique email and phone numbers
- Case-insensitive email duplicate checking

**Note:** This uses in-memory storage. Data resets between serverless invocations.
## Project Structure

```
├── app/
│   ├── routes.py           # API routes
│   ├── services.py         # Business logic
├── data/
│   └── employees.json      # Data store
├── tests/
│   ├── unit_tests.py       # Route tests
│   └── integration_tests.py # Service tests
├── run.py                  # Entry point
└── postman_collection.json
```