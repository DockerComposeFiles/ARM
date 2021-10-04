FROM arm32v7/python:rc-buster AS py-base
# Updaten des Images
RUN apt update && apt -y upgrade
# Debug Programme
RUN apt install nano tree lynx iputils-ping -y

FROM py-base AS py-debug
# Bibliotheken
RUN apt install python python-dev python-pip
RUN apt install build-essential python-setuptools apt-utils i2c-tools python-smbus -y
# I2C ist nur mit python 2 smbus kompatibel
RUN pip install smbus Adafruit_BBIO

FROM py-debug AS py-i2c
ARG environment=py-htu
# Zugriff auf den HTU21D
#RUN apt install python3 python3-pip
RUN pip install adafruit-circuitpython-HTU21D
#RUN pip install --no-cache-dir -r requirements.txt
COPY script.py /
RUN chmod +x script.py
# Initialisieren / Überprfuefen der GPIO
CMD ["python", "script.py"]
