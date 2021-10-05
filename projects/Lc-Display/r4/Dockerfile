FROM arm32v7/python:rc-buster AS debug

# Updaten des Images
RUN apt update && apt -y upgrade
# Debug Programme
RUN apt install -y nano && apt install tree && apt install -y lynx && apt install -y iputils-ping

FROM debug AS rpi
# Bibliotheken
#RUN apt install -y apt-utils i2c-tools python-smbus
RUN apt install rpi.gpio

FROM rpi AS lc


RUN apt clean
WORKDIR /
COPY script.py /
RUN chmod +x script.sh
CMD [ "python", "./script.py" ]
