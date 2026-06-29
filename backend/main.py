from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager

from core.db import create_db
from router.account_router import router as account_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/ping")
def ping():
    return "pong"

app.include_router(
    account_router,
    prefix="/api"
)
