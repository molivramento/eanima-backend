from dashboard.users.customers.models import Customer

CustomerIn = Customer.get_pydantic(
    exclude={
        'id': ...
    }
)
