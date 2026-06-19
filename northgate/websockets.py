import json
from fastapi import WebSocket, WebSocketDisconnect

from .logger import logger
from .constants import LOAD_LOCAL_SITES, ERROR_MESSAGE
from northgate.database.sites import get_local_sites


def add_ws_endpoint(app):
    clients: list[WebSocket] = []

    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()
        clients.append(websocket)
        try:
            while True:
                data = await websocket.receive_text()
                decoded_data = json.loads(data)
                action = decoded_data.get("action")
                try:
                    # Loading local sites
                    if action == LOAD_LOCAL_SITES:
                        local_sites = get_local_sites()
                        local_sites_dict = [site.toDict() for site in local_sites]
                        logger.debug("Local sites loaded: {}".format(local_sites_dict))
                        await websocket.send_text(json.dumps({"action": LOAD_LOCAL_SITES, "data": local_sites_dict}))

                except Exception as e:
                    logger.error("Error processing action {}: {}".format(action, e))
                    await websocket.send_text(json.dumps({"action": ERROR_MESSAGE, "message": "Error: {}".format(e)}))

        except WebSocketDisconnect:
            clients.remove(websocket)
