#!/usr/bin/env python
# -*- coding: utf8 -*-
import time

import socketio
import os

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


# Warten, damit Apache bereit ist
time.sleep(10)


# Testen, ob Localhost (127.0.0.0, 127.0.0.1),
# die feste IP 172.24.0.2 und ? 0.0.0.0 verfügbar ist.
# Zugriff auf den Apache Server wird getestet
# Der Websocket läuft auf Port 3000

IPs = ["localhost", "127.0.0.0", "127.0.0.1", "172.24.0.2", "0.0.0.0",
       "127.0.0.0:3000", "127.0.0.1:3000", "172.24.0.2:3000", "0.0.0.0:3000"]
for e in IPs:
    response = os.system("ping -n 1 " + e)

    if response == 0:
        print(e, 'is up')
    else:
        print(e, 'is down')

# Mit Host Verbinden
sio.connect('http://172.24.0.2:3000/')

time.sleep(200)
