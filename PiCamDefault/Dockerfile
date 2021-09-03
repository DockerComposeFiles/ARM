FROM python:3

#RUN apt update
#RUN apt -y upgrade

# Kamera Bibliothek
RUN pip install picamera

# Ausführung des Hauptscriptes
ADD script.py /
RUN apt clean
CMD [ "python", "./script.py" ]
