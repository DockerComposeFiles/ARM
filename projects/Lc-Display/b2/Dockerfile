FROM arm32v7/python:rc-buster AS debug

# Updaten des Images
RUN apt update && apt -y upgrade
# Debug Programme
RUN apt install -y nano && apt install tree && apt install -y lynx && apt install -y iputils-ping

FROM debug AS i2c
# Bibliotheken
RUN apt install -y apt-utils i2c-tools python-smbus

FROM i2c AS htu21d
#RUN apt install python3 && apt install python3-pip
#RUN pip install adafruit-circuitpython-HTU21D
#RUN pip install --no-cache-dir -r requirements.txt

RUN apt clean
WORKDIR /
COPY script.py /
RUN chmod +x script.sh
CMD [ "python", "./script.py" ]
