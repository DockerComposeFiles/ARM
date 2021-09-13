FROM python:3

#RUN apt update
#RUN apt -y upgrade

# Python 2
RUN apt install python && apt install pip
# Kamera Bibliothek
RUN pip install picamera

# Ausführung des Hauptscriptes
ADD script.py /
RUN apt clean
CMD [ "python", "./script.py" ]
