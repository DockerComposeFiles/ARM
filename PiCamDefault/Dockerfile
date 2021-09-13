FROM python:3

#RUN apt update
#RUN apt -y upgrade

# Python 2 ist nicht notwendig
#RUN apt install python2 && apt install python-pip

# Kamera Bibliothek
RUN pip install picamera

# Ausführung des Hauptscriptes
ADD script.py /
RUN apt clean
CMD [ "python", "./script.py" ]
