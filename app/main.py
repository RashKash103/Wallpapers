from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI, Request
from fastapi.responses import Response

from utils import get_random_image


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.requests_client = httpx.AsyncClient()
    yield
    await app.requests_client.aclose()


app = FastAPI(lifespan=lifespan)


@app.get(
    "/{width}/{height}",
    responses={200: {"content": {"image/jpeg": {}}}},
    response_class=Response,
)
async def get_image(request: Request, width: int, height: int):
    img = await get_random_image(width, height, request.app.requests_client)
    return Response(content=img, media_type="image/jpeg")
