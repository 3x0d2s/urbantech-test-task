from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.views import router as views_router
from app.redis_client import redis_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await redis_client.close_connection()


app = FastAPI(lifespan=lifespan)

app.include_router(views_router, prefix='/api')


@app.get("/")
def read_root():
    return {"Hello": "World"}
