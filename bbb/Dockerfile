FROM arm32v7/python:3.10.0rc2-slim-buster AS base

RUN apt update
RUN apt -y upgrade
# Debug Programme
RUN apt install -y nano && apt install tree

FROM base AS driver

# Bibliotheken
RUN apt install -y apt-utils i2c-tools python-smbus

FROM driver
RUN pip3 install adafruit-circuitpython-htu21d
ADD /config.sh /
RUN sh ./config.sh

# Script zum sammeln der Daten
ADD /script.py /script.py
CMD [ "python3", "./script.py" ]
