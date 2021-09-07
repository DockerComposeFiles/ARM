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
    print("The connection failed: " + err)


@sio.event
def disconnect():
    print("I'm disconnected!")

# Testen, ob Apache verfügbar ist
import os

hostname = "localhost"
response = os.system("ping -n 1 " + hostname)

if response == 0:
    print(hostname, 'is up!')
else:
    print(hostname, 'is down!')

sio.connect('http://localhost:3000/')
