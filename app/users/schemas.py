from app.users.models import User
from app.users.providers.models import Provider
from app.users.employees.models import Employee
from app.users.customers.models import Customer

UserIn = User.get_pydantic(
    exclude={
        'id': ...,
        'active': ...,
        'verified': ...,
        'only_provider': ...,
        'providers': ...,
        'employees': ...,
        'role': ...,
        'permission': ...,
        'customers': ...,
        'groups': ...,
        'admin': ...
    }
)

UserOut = User.get_pydantic(
    exclude={
        'password': ...
    }
)
