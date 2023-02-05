from app.users.models import User
from app.users.providers.models import Provider
from app.users.employees.models import Employee

UserIn = User.get_pydantic(
    exclude={
        'id': ...,
        'active': ...,
        'verified': ...,
        'only_provider': ...,
        'providers': ...,
        'employees': ...
    }
)

UserOut = User.get_pydantic(
    exclude={
        'password': ...,
    }
)
