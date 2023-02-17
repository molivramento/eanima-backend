from fastapi import APIRouter

from app.users.schemas import UserIn

router = APIRouter()


@router.post('/token/')
async def get_token(user: UserIn):
    pass
