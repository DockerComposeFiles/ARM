#!/usr/bin/env python
# -*- coding: utf8 -*-

import socketio

# standard Python
sio = socketio.Client()

# asyncio
asio = socketio.AsyncClient()


# Event handler
@sio.on('*')
def catch_all(event, sid, data):
    pass


@sio.on('*')
async def catch_all(event, sid, data):
    pass


@sio.event
def connect():
    print("I'm connected!")


@sio.event
def connect_error(err):
    print("The connection failed:" + err)


@sio.event
def disconnect():
    print("I'm disconnected!")


sio.connect('http://localhost:3000/')
