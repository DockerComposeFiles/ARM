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
    print("I'm connected!", flush=True)


@sio.event
def connect_error(err):
    print("The connection failed: " + err, flush=True)


@sio.event
def disconnect():
    print("I'm disconnected!", flush=True)


# Warten, damit Apache bereit ist
# time.sleep(20)

# Testen, welche Verbindungen (Apache Server) verfügbar sind
# Internet down?, Localhost=127.0.0.1 ok, 127.24.0.5 ok
# 0.0.0.0 ok, 172.24.0.0-subnet ok, 172.24.0.1-gateway ok
# Der Websocket läuft auf Port 3000 und IPs 5, 2

IPs = ["https://duckduckgo.com", "localhost", '127.24.0.0', '127.24.0.1', '172.24.0.5', '0.0.0.0',
       '172.24.0.5:3000', '172.24.0.2', '172.24.0.2:3000']

for e in IPs:
    # Ping Abfrage, um die Verfügbarkeit zu testen
    response = os.system("ping -n -c 1 " + e)

    # Standard Zeitintervall zwischen den PING Ausführungen
    time.sleep(1)

    if response == 0:
        print(e, 'is up: ' + str(response) + '\n', flush=True)
    else:
        print(e, 'is down: ' + str(response) + '\n', flush=True)

print("create connection", flush=True)
# Mit Host Verbinden
sio.connect('http://172.24.0.2:3000/')

time.sleep(10)
