from schemas import STaskAdd
from database import create_tables, delete_tables
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional
from contextlib import asynccontextmanager
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
