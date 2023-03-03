from uuid import UUID

from fastapi import APIRouter

from dashboard.users.customers.models import Customer
from dashboard.users.customers.schemas import CustomerIn

router = APIRouter()


@router.post('/')
async def create_customer(payload: CustomerIn):
    return Customer.objects.create(**payload.dict())


@router.get('/', response_model=list[Customer])
async def get_customers():
    return Customer.objects.all()


@router.get('/{customer_id}/', response_model=Customer)
async def get_customer(customer_id: UUID):
    return await Customer.objects.get_or_none(id=customer_id)


@router.put('/')
async def update_customer(payload: Customer):
    provider = Customer.objects.get_or_none(id=payload.id)
    return provider.update(**payload.dict())


@router.delete('/')
async def provider_customer(customer_id: UUID):
    provider = Customer.objects.get_or_none(id=customer_id)
    return provider.delete()
