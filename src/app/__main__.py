import typer
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.exceptions import RequestValidationError

from app.routers import ping
from app.uvicorn_helpers import UvicornConfig, UvicornServer
from app.env import SERVER_PORT
from app.exceptions import handlers


server_app = FastAPI()
server_app.get("/")(lambda: RedirectResponse(url="/docs"))
server_app.include_router(
    ping.router,
)

server_app.add_exception_handler(RequestValidationError, handlers.exception_422)

app = typer.Typer()

@app.command()
def cli(
    host: str = typer.Option(
        "0.0.0.0",
        metavar="host",
        help="host",
    ),
    port: int = typer.Option(
        SERVER_PORT,
        metavar="port",
        help="port",
    ),
    debug: bool = typer.Option(False, metavar="debug", help="debug"),
    reload: bool = typer.Option(False, metavar="reload", help="reload"),
):
    config = UvicornConfig(
        server_app,
        host=host,
        port=port,
        log_level="info",
        reload=reload,
        reload_dirs=["/workspace/src/app"] if debug else [],
    )
    server = UvicornServer(config=config)
    server.run()


app()
