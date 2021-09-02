FROM balenalib/raspberrypi3-debian:latest
RUN apt update
RUN apt install -y nano

# Kamera Bibliothek
RUN pip install picamera

# Ausführung des hauptscriptes
ADD script.py /
RUN apt clean
CMD [ "python", "./script.py" ]
