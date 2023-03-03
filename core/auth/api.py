from fastapi import APIRouter, Request, Depends

from core.auth.cryptography import encode, decode
from core.auth.deps import JWTBearer
from core.auth.utils import uuid_auth

from dashboard.users.models import User
from dashboard.users.schemas import UserIn

router = APIRouter()


@router.post('/token/')
async def get_token(payload: UserIn):
    user = await User.objects.get_or_none(email=payload.email)
    if user:
        token = encode(data={'id': str(user.id), 'email': user.email})
        return {'access_token': token['access_token'], 'refresh_token': token['refresh_token']}


@router.post('/me', dependencies=[Depends(JWTBearer())])
async def get_me(request: Request):
    print(request.headers)
    return await User.objects.get_or_none(id=uuid_auth(request))


@router.post('/refreshToken')
async def get_refresh_token(request: Request):
    refresh_token = request.headers.get('authorization').split()[1]
    return decode(refresh_token=refresh_token)
