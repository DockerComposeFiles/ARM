FROM arm32v7/python:rc-buster AS py-base
# Updaten des Images
RUN apt update && apt -y upgrade
# Debug Programme
RUN apt install -y nano tree lynx iputils-ping

FROM arm32v7/golang:rc-bullseye AS go-base
RUN apt update && apt -y upgrade
RUN apt install -y nano tree lynx iputils-ping

FROM arm32v7/bullseye AS base
RUN apt update && apt -y upgrade
RUN apt install -y nano tree lynx iputils-ping



FROM py-base AS py-debug
# Bibliotheken
RUN apt install -y apt-utils i2c-tools python-smbus
#RUN pip3 install smbus

FROM go-base AS go-debug
RUN apt install -y apt-utils i2c-tools python-smbus

FROM base AS debug
RUN apt install -y apt-utils i2c-tools python-smbus



FROM py-debug AS py-i2c
FROM py-i2c AS py-htu
# Zugriff auf den HTU21D
#RUN apt install python3 python3-pip
RUN pip install adafruit-circuitpython-HTU21D
#RUN pip install --no-cache-dir -r requirements.txt
COPY script.py /
RUN chmod +x script.py
# Initialisieren / Überprfuefen der GPIO
CMD ["python", "script.py"]

FROM go-debug AS go-i2c
# TODO go-bib for ctrl
# TODO go-lib blink

FROM debug AS shell-i2c
COPY script.sh /
RUN chmod +x script.sh
CMD ./script.sh

FROM debug AS c-i2c
RUN apt install -y git && mkdir development && cd development
RUN git clone https://github.com/shabaz123/iobb.git
RUN cd iobb && make && make install

FROM debug AS c-i2c_local
COPY iofunc/* /
#RUN gcc pin_2.c -iofunc -o main
