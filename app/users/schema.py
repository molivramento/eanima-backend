from app.users.models import User

UserIn = User.get_pydantic(
    exclude={
        'id': ...,
        'active': ...,
        'verified': ...,
        'only_provider': ...
    }
)

UserOut = User.get_pydantic(
    exclude={
        'password': ...
    }
)
