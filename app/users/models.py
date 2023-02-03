import ormar

from uuid import UUID

from config.database import BaseMeta


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'users'

    id: UUID = ormar.UUID(primary_key=True, editable=False)
    email: str = ormar.String(max_length=255, unique=True)
    password: str = ormar.String(max_length=255)
    only_provider: bool = ormar.Boolean()
    active: bool = ormar.Boolean(default=True)
    verified: bool = ormar.Boolean(default=False)
