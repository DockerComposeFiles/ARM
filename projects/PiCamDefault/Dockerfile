# Genaue Image Angabe
FROM arm32v7/python:3.10.0rc2-slim-buster
# Ungefähre Image Angabe. Wählt Debian:bullseye als Distro -> apt funktioniert nicht
#FROM python:3

RUN apt update
RUN apt -y upgrade

# Die Picamera Bibliothek kann alternativ unter Python 2 ab Version 2.7 verwendet werden
#RUN apt install python2 && apt install python-pip

# Installation der Kamera-Bibliothek
# picamera stellt ausschließlich die neueste version unter den Python
#RUN pip install picamera

# Manuelle Installation.
## Deaktivierung der Abfrage der Systemvariablen
RUN export READTHEDOCS=true

## Der picamera Quellcode wurde mittels SPC direkt an den Raspberry übertragen
## und befindet sich daher nicht im Repository.
WORKDIR /
RUN mkdir "/picam"
COPY picam /picam

# Installer Ausführungsberechtigungen geben
RUN chmod -+X picam/setup.py
# Gesamten Ordner Ausführungsberechtigungen geben
RUN chmod -R +X picam
# Installation der Bibliothek
RUN bash picam/setup.py

# Ausführung des Hauptscriptes
ADD script.py /
RUN apt clean
CMD [ "python", "./script.py" ]
