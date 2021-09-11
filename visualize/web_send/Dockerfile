FROM arm32v7/debian:buster-slim AS base

# Behebt Fehler
RUN apt clean
# Updaten des Images
RUN apt update && apt -y upgrade
# Debug Programme
RUN apt install -y nano && apt install tree && apt install -y lynx && apt install -y iputils-ping

FROM base AS python_backend

# Installieren von Python (angepasste Version)
RUN apt install -y python3.7 && apt install -y python-pip && apt install -y python3-pip

# Bibliothek zum senden der Daten
RUN pip3 install "python-socketio[client]"
RUN pip3 install "python-socketio[asyncio_client]"

RUN apt clean

FROM python_backend

# Anlegen des Volume Ordners zum späteren Mounten
RUN mkdir /data

# Zurücksetzen des Arbeitsverzeichnisses
WORKDIR /

# send_data wird des öfteren geändert
# Der Docker context erkennt diese Änderungen nicht
# Cacheburst deaktiviert das cachen ab diesem Layer
ARG CACHEBUST=1
ADD send_data.py /
CMD ["python3", "./send_data.py"]

RUN echo("im_alive")
# Port ist ebenfalls im compose Festgelegt
#EXPOSE 3000
