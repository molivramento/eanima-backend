from fastapi import FastAPI

from config.database import database, config_database

from app.users.api import router as users
from app.users.providers.api import router as providers
from app.users.employees.api import router as employees
from app.users.customers.api import router as customers

app = FastAPI()

app.include_router(users, prefix='/users', tags=['Users'])
app.include_router(providers, prefix='/providers', tags=['Users - Providers'])
app.include_router(customers, prefix='/customers', tags=['Users - Customers'])
app.include_router(employees, prefix='/employees', tags=['Users - Employees'])

app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()
    config_database()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()
