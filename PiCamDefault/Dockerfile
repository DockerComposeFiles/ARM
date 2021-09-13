FROM arm32v7/python:rc-buster

#RUN apt update
#RUN apt -y upgrade

# Python 2 ist nicht notwendig
#RUN apt install python2 && apt install python-pip

# Kamera Bibliothek kann nicht
#RUN pip3 install picamera

#Manuelle Installation
WORKDIR /
RUN mkdir "/picam3"
COPY picam3 /picam3
# Installer Ausführungsberechtigungen geben
RUN chmod -+X picam3/setup.py
# Gesamten Ordner Ausführungsberechtigungen geben
RUN chmod -R +X picam3
# Installieren
RUN bash picam3/setuo.py

# Ausführung des Hauptscriptes
ADD script.py /
RUN apt clean
CMD [ "python", "./script.py" ]
