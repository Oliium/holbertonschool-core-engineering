#!/usr/bin/env python3
"""A WebSocket server that replies only to the sender (unicast, U: prefix)."""
import asyncio

import websockets
from websockets.exceptions import ConnectionClosed

CLIENTS = set()


async def connection_handler(websocket):
    """Track the client and echo each message back to it with a U: prefix."""
    CLIENTS.add(websocket)
    try:
        async for message in websocket:
            await websocket.send("U:" + message)
    except ConnectionClosed:
        pass
    finally:
        CLIENTS.discard(websocket)


async def main():
    """Start the unicast server on localhost:8765 and run forever."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())
