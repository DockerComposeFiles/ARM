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

# Testen, ob Localhost (127.0.0.1) verfügbar ist
hostname = "localhost"
response = os.system("ping -n 1 " + hostname)

if response == 0:
    print(hostname, 'is up!')
else:
    print(hostname, 'is down!')
# localhost funktioniert nicht, um den Apache anzusprechen

# Testen ob die feste IP verfügbar ist
ipname = "172.24.0.2:3000"
response = os.system("ping -n 1 " + ipname)

if response == 0:
    print(ipname, 'is up!')
else:
    print(ipname, 'is down!')
# Apache ist unter der festgelegten IP nicht verfügbar

# Testen ob Apache unter 127.0.0.1 verfügbar ist
lh = "127.0.0.1:3000"
response = os.system("ping -n 1 " + lh)

if response == 0:
    print(lh, 'is up!')
else:
    print(lh, 'is down!')
# ?

# Mit Host Verbinden
sio.connect('http://0.0.0.0:3000/')

time.sleep(10)
