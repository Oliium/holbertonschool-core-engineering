#!/usr/bin/env python3
"""A minimal WebSocket client that sends one message and returns the reply."""
import asyncio
import os
import sys

import websockets


async def connect_and_send(uri, message):
    """Connect to uri, send message, and return the server's response."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        return await websocket.recv()


def main():
    """Read uri/message from env or CLI and print the echoed response."""
    uri = os.environ.get("WS_URI", "ws://localhost:8765")
    if len(sys.argv) > 1:
        message = sys.argv[1]
    else:
        message = os.environ.get("WS_MESSAGE", "demo")
    response = asyncio.run(connect_and_send(uri, message))
    sys.stdout.write(response)


if __name__ == "__main__":
    main()
