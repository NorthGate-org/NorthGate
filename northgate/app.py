import os
import webbrowser
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .logger import logger


def application(web_port):
    async def callback():
        webbrowser.open(f"http://127.0.0.1:{web_port}")

    app = FastAPI(on_startup=[callback])

    # Add static file route for the web interface
    app.mount("/static", StaticFiles(directory="northgate/web/static"), name="static")

    @app.get("/")
    async def index():
        return FileResponse('northgate/web/index.html', media_type='text/html')
    
    return app

def start_server(app, web_port, log_level):
    config = uvicorn.Config(app, port=web_port, log_level=log_level.lower())
    server = uvicorn.Server(config)
    try:
        logger.info("Starting NorthGate web server on port {}...".format(web_port))
        server.run()
    except KeyboardInterrupt:
        logger.info("Shutting down NorthGate web server...")
    except Exception as e:
        logger.error("Error occurred while running the server: {}".format(e))
