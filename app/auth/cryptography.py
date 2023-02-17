import time

from decouple import config
from datetime import datetime, timedelta
from jose import jwt, JWTError

ALGORITHM = 'HS256'
SECRET_ACCESS_TOKEN = config('SECRET_ACCESS_TOKEN')
SECRET_REFRESH_TOKEN = config('SECRET_REFRESH_TOKEN')
ACCESS_TOKEN_EXPIRE_MINUTES = int(config('ACCESS_TOKEN_EXPIRE_MINUTES'))
REFRESH_TOKEN_EXPIRES_MINUTES = int(config('REFRESH_TOKEN_EXPIRES_MINUTES'))


def encode(data: dict):
    enc = data.copy()
    access_expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_expire = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRES_MINUTES * 24 * 2)
    enc.update({'exp': access_expire})
    access_token = jwt.encode(enc, SECRET_ACCESS_TOKEN, ALGORITHM)
    enc.update({'exp': refresh_expire})
    refresh_token = jwt.encode(enc, SECRET_ACCESS_TOKEN, ALGORITHM)
    return {'access_token': access_token, 'refresh_token': refresh_token}


def decode(access_token: str | None = None, refresh_token: str | None = None):
    if access_token:
        decoded = jwt.decode(access_token, SECRET_ACCESS_TOKEN, ALGORITHM)
        if float(decoded['exp']) > time.time():
            return decoded
    if refresh_token:
        decoded = jwt.decode(refresh_token, SECRET_REFRESH_TOKEN, ALGORITHM)
        if float(decoded['exp']) > time.time():
            return encode(data={'id': str(decoded['id']), 'email': decoded['email']})