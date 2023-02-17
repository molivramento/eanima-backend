from app.users.schemas import UserIn
from app.users.utils import get_user


def authenticate_user(user: UserIn):
    return await get_user(user)
