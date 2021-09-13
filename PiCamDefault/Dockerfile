FROM arm32v7/python:rc-buster

#RUN apt update
#RUN apt -y upgrade

# Python 2 ist nicht notwendig
#RUN apt install python2 && apt install python-pip

# Systemvariable, um die Prüfung des System auf PI-OS zu deaktivieren.
RUN export READTHEDOCS=True

# Kamera Bibliothek
RUN pip3 install picamera

# Ausführung des Hauptscriptes
ADD script.py /
RUN apt clean
CMD [ "python", "./script.py" ]
