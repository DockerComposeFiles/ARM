#FROM arm32v7/python:rc-buster
FROM python:3
RUN apt update
#RUN apt -y upgrade

# Die Picamera Bibliothek kann alternativ unter Python 2 ab Version 2.7 verwendet werden
#RUN apt install python2 && apt install python-pip

# Installation der Kamera-Bibliothek
# picamera stellt ausschließlich die neueste version unter den Python
RUN pip install picamera

# Manuelle Installation.
# Der modifizierte picamera Quellcode wurde mittels SPC direkt an den Raspberry übertragen.
WORKDIR /
RUN mkdir "/picam"
COPY picam3 /picam3
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
