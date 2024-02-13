import multiprocessing

import uvicorn


class UvicornConfig(uvicorn.Config):
    @property
    def should_reload(self) -> bool:
        return self.reload


class UvicornServer(multiprocessing.Process):
    def __init__(self, config: UvicornConfig):
        super().__init__()

        self.config = config

    def stop(self):
        self.terminate()

    def run(self, *args, **kwargs):
        server = uvicorn.Server(config=self.config)
        server.run()
