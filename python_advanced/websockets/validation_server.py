#!/usr/bin/env python3
"""A WebSocket server that validates messages before echoing them back."""
import asyncio

import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """Validate each message, replying OK:<msg> or ERR:EMPTY, forever."""
    try:
        async for message in websocket:
            if message.strip():
                await websocket.send("OK:" + message)
            else:
                await websocket.send("ERR:EMPTY")
    except ConnectionClosed:
        pass


async def main():
    """Start the validation server on localhost:8765 and run forever."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())
