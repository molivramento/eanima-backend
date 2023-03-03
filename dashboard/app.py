from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.auth.api import router as auth
from dashboard.users.api import router as users
from dashboard.categories.api import router as categories
from dashboard.users.providers.api import router as providers
from dashboard.users.employees.api import router as employees
from dashboard.users.customers.api import router as customers

app = FastAPI()

app.include_router(auth, prefix='/auth', tags=['Auth'])
app.include_router(users, prefix='/users', tags=['Users'])
app.include_router(categories, prefix='/categories', tags=['Categories'])
app.include_router(providers, prefix='/providers', tags=['Users - Providers'])
app.include_router(customers, prefix='/customers', tags=['Users - Customers'])
app.include_router(employees, prefix='/employees', tags=['Users - Employees'])



origins = [
    "http://localhost",
    "http://localhost:9000",
    "http:127.0.0.1:9000",
    "http://localhost:8000",
    "http:127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
