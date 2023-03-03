from uuid import uuid4

from config.crud import CRUD


class Categories(CRUD):
    async def create_related(self, payload, parent_id):
        parent = await CRUD.get(self, parent_id)
        return await self.table.objects.create(**payload.dict(), id=uuid4(), parent_id=parent)
