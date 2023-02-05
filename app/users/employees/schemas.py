from app.users.employees.models import Employee

EmployeeIn = Employee.get_pydantic(
    exclude={
        'id': ...,
        'user': ...
    }
)