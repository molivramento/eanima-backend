from typing import Optional

import ormar
from uuid import UUID
from config.database import BaseMeta
from pydantic.typing import ForwardRef

CategoryRef = ForwardRef('Category')


class Category(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'categories'

    id: UUID = ormar.UUID(primary_key=True, editable=False)
    name: str = ormar.String(max_length=255, unique=True)
    slug: str = ormar.String(max_length=255)
    description: str = ormar.Text()
    active: bool = ormar.Boolean(default=True)
    parent: Optional[CategoryRef] = ormar.ForeignKey(CategoryRef, nullable=True)


Category.update_forward_refs()
