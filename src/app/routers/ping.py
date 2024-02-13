from fastapi import APIRouter

from app.meta.api import (
    PingResponse,
    PingInput
)

router = APIRouter()


@router.get("/ping", response_model=PingResponse)
async def get_ping():
    response = "hey hey hey!"
    return PingResponse(message=response)

@router.post("/ping", response_model=PingResponse)
async def get_ping(ping_input: PingInput):
    response = "hey hey hey!"
    return PingResponse(message=response)