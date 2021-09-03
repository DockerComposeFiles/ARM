#!/usr/bin/env python
# -*- coding: utf8 -*-

import asyncio
import websockets

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()

try:
    asyncio.get_event_loop().run_until_complete(
        hello('ws://localhost:80'))
    print("script.js finish")

except:
    exec

