from uuid import UUID

import ormar

from config.database import BaseMeta

from dashboard.users.models import User


class Employee(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'employees'

    id: UUID = ormar.UUID(primary_key=True)
    user: User = ormar.ForeignKey(User)
    position: str = ormar.String(max_length=16)
