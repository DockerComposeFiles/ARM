FROM arm32v7/python:rc-buster

#RUN apt update
#RUN apt -y upgrade

# Python 2 ist nicht notwendig
#RUN apt install python2 && apt install python-pip

# Kamera Bibliothek kann nicht
#RUN pip3 install picamera

#Manuelle Installation
WORKDIR /
COPY picamera-release-1.10 /

# Installer Ausführungsberechtigungen geben
RUN chmod -+X /picamera-release-1.10/setuo.py
# Gesamten Ordner Ausführungsberechtigungen geben
RUN chmod -R +X /picamera-release-1.10
# Installieren
RUN bash /picamera-release-1.10/setuo.py

# Ausführung des Hauptscriptes
ADD script.py /
RUN apt clean
CMD [ "python", "./script.py" ]
