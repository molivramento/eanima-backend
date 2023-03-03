from dashboard.users.models import User
from dashboard.users.providers.models import Provider
from dashboard.users.employees.models import Employee
from dashboard.users.customers.models import Customer

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
