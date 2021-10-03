FROM arm32v7/python:rc-buster AS python-base
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



FROM python-base AS python-debug
# Bibliotheken
RUN apt install -y apt-utils i2c-tools python-smbus
#RUN pip3 install smbus

FROM go-base AS go-debug
RUN apt install -y apt-utils i2c-tools python-smbus

FROM base AS debug
RUN apt install -y apt-utils i2c-tools python-smbus



FROM python-debug AS python-i2c
#RUN apt install python3 && apt install python3-pip
RUN pip install adafruit-circuitpython-HTU21D
#RUN pip install --no-cache-dir -r requirements.txt
COPY script.py /
RUN chmod +x script.py
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
#RUN gcc pin_2.c -iofunc -o main
