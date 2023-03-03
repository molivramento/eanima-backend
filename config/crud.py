from uuid import uuid4


class CRUD:
    def __init__(self, table):
        self.table = table

    async def create(self, payload):
        return await self.table.objects.create(**payload.dict(), id=uuid4())

    async def all(self, relates):
        return await self.table.objects.prefetch_related(relates).all()

    async def get(self, pk):
        return await self.table.objects.get_or_none(id=pk)

    async def update(self, payload):
        category = await self.table.objects.get_or_none(id=payload.id)
        return await category.update(**payload.dict())

    async def delete(self, payload):
        category = await self.table.objects.get_or_none(id=payload)
        return await category.delete()
