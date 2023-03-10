from uuid import UUID, uuid4

from fastapi import APIRouter

from dashboard.users.models import User
from dashboard.users.providers.models import Provider
from dashboard.users.providers.schemas import ProviderIn

router = APIRouter()


@router.get('/user/{user_id}/')
async def get_providers(user_id: UUID):
    return await Provider.objects.filter(user__id=user_id).all()


@router.get('/{provider_id}/', response_model=Provider)
async def get_provider(provider_id: UUID):
    return await Provider.objects.get_or_none(id=provider_id)


@router.post('/')
async def create_provider(payload: ProviderIn, user_id: UUID):
    user = await User.objects.get_or_none(id=user_id)
    return await Provider.objects.create(**payload.dict(), id=uuid4(), user=user)


@router.put('/')
async def update_provider(payload: Provider):
    provider = Provider.objects.get_or_none(id=payload.id)
    return provider.update(**payload.dict())


@router.delete('/')
async def delete_provider(provider_id: UUID):
    provider = Provider.objects.get_or_none(id=provider_id)
    return provider.delete()
