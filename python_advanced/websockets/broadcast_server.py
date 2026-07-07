#!/usr/bin/env python3
"""A WebSocket server that broadcasts each message to all clients (B:)."""
import asyncio

import websockets
from websockets.exceptions import ConnectionClosed

CLIENTS = set()


async def connection_handler(websocket):
    """Track the client and forward each message to every active client."""
    CLIENTS.add(websocket)
    try:
        async for message in websocket:
            websockets.broadcast(CLIENTS, "B:" + message)
    except ConnectionClosed:
        pass
    finally:
        CLIENTS.discard(websocket)


async def main():
    """Start the broadcast server on localhost:8765 and run forever."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())
