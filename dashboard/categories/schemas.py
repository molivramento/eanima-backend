from enum import Enum

from dashboard.categories.models import Category

CategoryIn = Category.get_pydantic(
    exclude={
        'id': ...,
        'categorys': ...,
        'parent': ...
    }
)

CategoryUpdate = Category.get_pydantic(
    exclude={
        'categorys': ...
    }
)

CategoryOut = Category.get_pydantic(
    exclude={
        'category': ...
    }
)


class FilterEnum(str, Enum):
    id = 'id',
    name = 'name',
    slug = 'slug'
