from dashboard.users.providers.models import Provider

ProviderIn = Provider.get_pydantic(
    exclude={
        'id': ...,
        'user': ...
    }
)
