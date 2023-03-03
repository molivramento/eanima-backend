import ormar
from uuid import UUID
from config.database import BaseMeta


class Store(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'stores'

    id: UUID = ormar.UUID(primary_key=True, editable=False)
    name: str = ormar.String(max_length=255)
    cnpj: str = ormar.String(max_length=20)
    address: str = ormar.String(max_length=255)
    neighborhood: str = ormar.String(max_length=70)
    city: str = ormar.String(max_length=50)
    uf: str = ormar.String(max_length=2)
    longitude: str = ormar.String(max_length=12)
    latitude: str = ormar.String(max_length=12)
