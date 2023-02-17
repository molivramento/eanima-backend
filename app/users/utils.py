from app.users.models import User
from app.users.schemas import UserOut


async def get_user(email: str) -> UserOut:
    return await User.objects.get_or_none(email=email)
