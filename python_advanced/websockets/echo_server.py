#!/usr/bin/env python3
"""A minimal WebSocket server that echoes back every message it receives."""
import asyncio

import websockets


async def connection_handler(websocket):
    """Handle one client connection, echoing each incoming message."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the WebSocket server on localhost:8765 and run forever."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())
