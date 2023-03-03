from uuid import UUID, uuid4
from fastapi import APIRouter, HTTPException, status

from dashboard.users.models import User
from dashboard.users.schemas import UserIn, UserOut
from core.auth.hash import hash_password

router = APIRouter()


@router.post('/')
async def create_user(payload: UserIn):
    user = await User.objects.get_or_none(email=payload.email)
    hashed_password = hash_password(payload.password)
    if user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'This email already registered')
    return await User.objects.create(email=payload.email,
                                     id=uuid4(),
                                     only_provider=False,
                                     password=hashed_password)


@router.get('/', response_model=list[UserOut])
async def get_users():
    return await User.objects.prefetch_related(['providers']).order_by('email').all()


@router.get('/{user_id}/', response_model=UserOut)
async def get_user(user_id: UUID):
    return await User.objects.get_or_none(id=user_id)


@router.put('/')
async def update_user(payload: UserOut):
    user = await User.objects.get_or_none(id=payload.id)
    return await user.update(**payload.dict())


@router.delete('/')
async def delete_user(payload: UserOut):
    user = await User.objects.get_or_none(id=payload.id)
    return await user.delete()

