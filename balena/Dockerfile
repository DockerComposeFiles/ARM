# specify the node base image with your desired version node:<version>
#FROM balenalib/raspberry-pi2-alpine-node:latest

FROM balenalib/raspberrypi3-debian:latest
RUN apt update
RUN apt install -y nano

# Kamera Bibliothek
RUN pip install picamera

# Ausführung des Hauptscriptes
ADD script.py /
RUN apt clean
CMD [ "python", "./script.py" ]

# Anwendungport
EXPOSE 8888