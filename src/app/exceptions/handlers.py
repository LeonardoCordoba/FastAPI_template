from functools import wraps
from json import JSONDecodeError

from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError


async def get_request_input(request: Request) -> tuple[dict, dict]:
    try:
        body = await request.json()
    except JSONDecodeError:
        body = {}
    query_params = dict(request.query_params.items())
    return jsonable_encoder(body), query_params


def get_exception_name(exception: Exception) -> str:
    return exception.__class__.__name__


def exception_handler(func: callable) -> callable:
    @wraps(func)
    async def wrapper(request, exc) -> JSONResponse:
        name = get_exception_name(exc)
        body, query_params = await get_request_input(request)
        status_code, mssg = func(exc)
        return JSONResponse(
            status_code=status_code,
            content={
                "status_code": status_code,
                "error": name,
                "message": mssg,
                "request": {"body": body, "query_params": query_params},
            },
        )

    return wrapper

@exception_handler
def exception_422(exc: RequestValidationError) -> tuple[int, str]:
    errors = exc.errors()
    mssg = "\n".join([f"{err.get('msg')}: {err.get('loc')}" for err in errors])
    return status.HTTP_422_UNPROCESSABLE_ENTITY, mssg
