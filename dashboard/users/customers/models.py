from uuid import UUID

import ormar

from dashboard.users.models import User
from config.database import BaseMeta


class Customer(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'customers'

    id: UUID = ormar.UUID(primary_key=True)
    user: User = ormar.ForeignKey(User)
    name: str = ormar.String(max_length=128)
    cpf: str = ormar.String(max_length=11)
    