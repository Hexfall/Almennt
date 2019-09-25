#!/usr/bin/env python

import asyncio
import websockets

async def hello():
    uri = "ws://localhost:6789/listings/1"
    async with websockets.connect(uri) as websocket:
        listing = await websocket.recv()
        print(listing)

asyncio.get_event_loop().run_until_complete(hello())
input()
