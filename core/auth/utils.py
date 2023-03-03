from uuid import UUID

from jose import JWTError
from core.auth.cryptography import decode
from fastapi.security import HTTPBearer
from fastapi import Request, Depends, HTTPException, status

from dashboard.users.models import User

oauth2_scheme = HTTPBearer()


def uuid_auth(request: Request):
    access_token = request.headers.get('authorization').split()[1]
    decoded_access_token = decode(access_token=access_token)
    return UUID(decoded_access_token['id'])


async def get_current_user(access_token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status.HTTP_401_UNAUTHORIZED, 'Cold not validate credentials')
    try:
        payload = decode(access_token)
        email = payload.get('email')
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await User.objects.get_or_none(email=email)
    if user is None or user.active is False:
        raise credentials_exception
    return user
