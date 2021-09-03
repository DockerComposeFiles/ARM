#!/usr/bin/env python
# -*- coding: utf8 -*-

import asyncio
import websockets

async def send_current(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()


asyncio.get_event_loop().run_until_complete(
    send_current('172.20.0.2:80'))
print("script.js finish")
