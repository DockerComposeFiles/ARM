FROM arm32v7/python:rc-buster AS base
# Behebt Fehler
RUN apt clean
# Updaten des Images
RUN apt update && apt -y upgrade
# Debug Programme
RUN apt install -y nano && apt install tree && apt install -y lynx && apt install -y iputils-ping

FROM base AS python_backend
# Bibliothek zum senden der Daten
RUN pip3 install "python-socketio[client]"
RUN pip3 install "python-socketio[asyncio_client]"

RUN apt clean

FROM python_backend

# Anlegen des Volume Ordners zum späteren Mounten
RUN mkdir /data

# Ausführung
ADD script.py /
CMD ["python3", "./script.py"]

# Port ist ebenfalls im compose Festgelegt
EXPOSE 3000