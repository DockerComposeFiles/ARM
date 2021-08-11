FROM arm32v7/python:rc-buster

RUN apt update
#RUN apt -y upgrade

# Kamera Bibliothek
RUN pip install picamera

# Ausführung des hauptscriptes
ADD script.py /
RUN apt clean
CMD [ "python", "./script.py" ]