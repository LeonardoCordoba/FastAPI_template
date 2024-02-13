from pydantic import BaseModel

class PingResponse(BaseModel):
    message: str

class PingInput(BaseModel):
    message: str
