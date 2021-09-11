import time
import socketio
import os

print("backend alive", flush=True)

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
    print("I'm connected!", flush=True)


@sio.event
def connect_error(err):
    print("The connection failed: " + err, flush=True)


@sio.event
def disconnect():
    print("I'm disconnected!", flush=True)


# Warten, damit Apache bereit ist
time.sleep(20)
print("go to ip test", flush=True)

# Testen, ob Localhost (127.0.0.0, 127.0.0.1),
# die feste IP 172.24.0.2 und ? 0.0.0.0 verfügbar ist.
# Zugriff auf den Apache Server wird getestet
# Der Websocket läuft auf Port 3000

IPs = ["localhost", "127.0.0.0", "127.0.0.1", "172.24.0.2", "0.0.0.0",
       "127.0.0.0:3000", "127.0.0.1:3000", "172.24.0.2:3000", "0.0.0.0:3000"]
for e in range(IPs):
    response = os.system("ping -n 1 " + e)

    if response == 0:
        print(e, 'is up', flush=True)
    else:
        print(e, 'is down', flush=True)

# Mit Host Verbinden
sio.connect('http://172.24.0.2:3000/')

time.sleep(10)
