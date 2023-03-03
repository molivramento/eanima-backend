from core.auth.cryptography import decode
from fastapi import status, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    detail='Invalid authentication scheme.'
                )
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    detail='Invalid token or expired token.'
                )
            return credentials.credentials
        else:
            raise HTTPException(
                status.HTTP_403_FORBIDDEN,
                detail='Invalid authorization code.'
            )

    def verify_jwt(self, token: str) -> bool:
        is_token_valid: bool = False
        try:
            payload = decode(access_token=token)
        except:
            payload = None
        if payload:
            is_token_valid = True
        return is_token_valid
