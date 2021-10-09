# Genaue Image Angabe
# Mittels einer für 'picamera' funktionablen Python-Version
FROM arm32v7/python:3.10.0rc2-slim-buster

# Ungefähre Image Angabe
# Unter dieser wird Debian:bullseye als Distrobution gewählt in welcher apt nicht arbeitet.
# FROM python:3

# Update der Paketquellen
RUN apt update && apt -y upgrade

# Deaktivierung der Abfrage der Systemvariablen
RUN export READTHEDOCS=true

## Die Picamera Bibliothek kann alternativ unter Python 2 ab Version 2.7 verwendet werden.
#  RUN apt install python2 python-pip picamera

## Installation der Kamera-Bibliothek
#  picamera stellt ausschließlich die neueste version in den Paketquellen bereit.
RUN pip3 install picamera

## Manuelle Installation.

# Mögliche Installation ueber git wuerde die Dateien-Anzahl und damit den Git-Head enorm erhoehen
# WORKDIR /
# RUN mkdir "/picam"
# COPY picam /picam

# Installer Ausführungsberechtigungen geben
# RUN chmod -+X picam/setup.py
# Gesamten Ordner Ausführungsberechtigungen geben
# RUN chmod -R +X picam
# Installation der Bibliothek
# RUN bash picam/setup.py

# Ausführung des Hauptscriptes
ADD script.py /
RUN chmod +x script.py
RUN apt clean
CMD [ "python", "./script.py" ]
