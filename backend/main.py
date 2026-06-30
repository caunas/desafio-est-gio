from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from core.db import create_db
from router.account_router import router as account_router
from router.operation_router import router as operation_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()

    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
def ping():
    return "pong"

app.include_router(
    account_router,
    prefix="/api"
)

app.include_router(
    operation_router,
    prefix="/api"
)
