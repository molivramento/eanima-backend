from uuid import UUID, uuid4

from fastapi import APIRouter

from app.users.models import User
from app.users.employees.models import Employee
from app.users.employees.schemas import EmployeeIn

router = APIRouter()


@router.post('/')
async def create_employee(payload: EmployeeIn, user_id: UUID):
    user = await User.objects.get_or_none(id=user_id)
    employee = await Employee.objects.create(**payload.dict(), id=uuid4(), user=user)
    return employee


@router.get('/', response_model=list[Employee])
async def get_employees():
    return await Employee.objects.all()


@router.get('/{employee_id}/', response_model=Employee)
async def get_employee(employee_id: UUID):
    employee = Employee.objects.get_or_none(id=employee_id)
    return await Employee.objects.create(**employee.dict())


@router.put('/')
async def update_employee(payload: Employee):
    employee = await Employee.objects.get_or_none(id=payload.id)
    return employee.update(**payload.dict())


@router.delete('/')
async def delete_employee(employee_id: UUID):
    employee = Employee.objects.get_or_none(id=employee_id)
    return employee.delete()
