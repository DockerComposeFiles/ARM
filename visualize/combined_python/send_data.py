#!/usr/bin/env python
# -*- coding: utf8 -*-

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


# Testen, ob Localhost verfügbar ist
hostname = "localhost"
response = os.system("ping -n 1 " + hostname)

if response == 0:
    print(hostname, 'is up!')
else:
    print(hostname, 'is down!')
# localhost funktioniert nicht, um den Apache anzusprechen

# Testen ob die feste IP verfügbar ist
ipname = "172.24.0.2"
response = os.system("ping -n 1 " + ipname)

if response == 0:
    print(ipname, 'is up!')
else:
    print(ipname, 'is down!')
# ?

# Mit Host Verbinden
sio.connect('http://localhost:3000/')
