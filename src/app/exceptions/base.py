from fastapi.exceptions import RequestValidationError

class MyCustomError(RequestValidationError): ...  # noqa
