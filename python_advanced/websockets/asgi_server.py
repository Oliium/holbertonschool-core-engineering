#!/usr/bin/env python3
"""A Starlette ASGI app serving an HTML page and a WebSocket echo endpoint."""
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect

PAGE = "<h1>WebSocket App</h1>"


async def homepage(request):
    """Return a simple HTML page for the root route."""
    return HTMLResponse(PAGE)


async def websocket_endpoint(websocket):
    """Accept the connection and echo every received message back."""
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
