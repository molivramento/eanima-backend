import ormar

from uuid import UUID

from config.database import BaseMeta

from app.users.models import User


class Provider(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'providers'

    id: UUID = ormar.UUID(primary_key=True, editable=False)
    user: User = ormar.ForeignKey(User)
    provider: str = ormar.String(max_length=10)
    provider_user_id: str = ormar.String(max_length=128)
    avatar: str = ormar.String(max_length=255)

