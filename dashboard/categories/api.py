from typing import Any
from uuid import UUID, uuid4

from fastapi import APIRouter

from dashboard.categories.models import Category
from dashboard.categories.schemas import CategoryIn, CategoryUpdate, FilterEnum

router = APIRouter()


@router.post('/')
async def create_category(payload: CategoryIn, parent: UUID | None = None):
    parent_id = await Category.objects.get_or_none(id=parent)
    return await Category.objects.create(id=uuid4(), **payload.dict(), parent=parent_id, categorys=parent_id)


@router.get('/', response_model=list[Category])
async def get_by_filter():
    return await Category.objects.select_related('parent').order_by('name').all()


@router.get('/parent/{category_id}', response_model=list[Category])
async def get_by_filter(category_id: UUID):
    return await Category.objects.order_by('name').filter(parent__id=category_id).all()


@router.put('/')
async def update_category(payload: CategoryUpdate):
    category = await Category.objects.get_or_none(id=payload.id)
    return await category.update(**payload.dict())


@router.delete('/')
async def delete_category(category_id: UUID):
    category = await Category.objects.get_or_none(id=category_id)
    return await category.delete()
