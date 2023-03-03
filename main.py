from fastapi import FastAPI

from config.database import config_database
from dashboard.app import app as dashboard
from config.database import database

app = FastAPI()

app.state.database = database

app.mount('/dashboard', dashboard)


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
