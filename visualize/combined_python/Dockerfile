FROM arm32v7/httpd AS python_def

# Updaten des Images
RUN apt update && apt -y upgrade
# Zum starten mehrerer Prozesse
RUN apt install -y supervisor
# Für Debug Zwecke
RUN apt install -y nano && apt install tree && apt install -y lynx

# Installieren von Python (letzte version)
RUN apt install -y python3.7 && apt install -y python-pip && apt install -y python3-pip

FROM python_def AS web_backend

# Bibliothek zum senden der Daten
RUN pip3 install "python-socketio[client]"
RUN pip3 install "python-socketio[asyncio_client]"

# Anlegen des Volume Ordners zum späteren Mounten
RUN mkdir /data

FROM web_backend AS website

# Apache Dateien und statische Webseite
COPY /htdocs/ /usr/local/apache2/htdocs/
COPY httpd.conf /usr/local/apache2/httpd.conf

RUN apt clean

## Ausführung des backend
WORKDIR /
# send_data wird des öfteren geändert, Cacheburst deaktiviert das cachen dieser Datei
ARG CACHEBUST=1
ADD send_data.py /
CMD ["python3", "./send_data.py"]

# Apache startet auch ohne diese Angabe
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

# Port ist im compose Festgelegt
EXPOSE 433 80
