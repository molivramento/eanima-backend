from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, status

from app.users.models import User
from app.users.schema import UserIn, UserOut

router = APIRouter()


@router.get('/', response_model=list[UserOut])
async def get_users():
    return await User.objects.order_by('email').select_all(follow=True).all()


@router.get('/{user_id}/', response_model=UserOut)
async def get_user(user_id: UUID):
    return await User.objects.get_or_none(id=user_id)


@router.post('/')
async def create_user(payload: UserIn):
    user = await User.objects.get_or_none(email=payload.email)
    if user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'This email already registered')
    return await User.objects.create(**payload.dict(), id=uuid4(), only_provider=False)


@router.put('/')
async def update_user(payload: UserOut):
    user = await User.objects.get_or_none(id=payload.id)
    return await user.update(**payload.dict())


@router.delete('/')
async def delete_user(payload: UserOut):
    user = await User.objects.get_or_none(id=payload.id)
    return await user.delete()

