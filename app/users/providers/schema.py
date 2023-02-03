from app.users.models import User
from app.users.providers.models import Provider

ProviderIn = Provider.get_pydantic(
    exclude={
        'id': ...,
        'user': ...
    }
)
