FROM arm32v7/python:rc-buster

# Container auf den neuesten Stand bringen
# Installation von benötigten und optionalen Paketen
RUN apt update \
#    && apt upgrade -y \
# I2C Tools
    && apt install apt-utils i2c-tools python-smbus \
# Python 2 (kann, kann, muss, muss)
    python python-pip python-dev python-rpi.gpio \
# Python3 (kann, kann, muss, muss)
    python3-pip python3 python3-dev python3-rpi.gpio \
# Erweiterte Tools
    build-essential nano -y \
    && apt clean

# Benötigte Python Bibliotheken, wenn Circuit verwendet
RUN pip install smbus Adafruit_BBIO
# No module named 'board' (AdaFruit): adafruit-blinka
RUN pip3 install setuptools adafruit-circuitpython-htu21d adafruit-blinka

# Benötigte Python Bibliotheken, wenn RPI verwendet
RUN pip install  RPi.GPIO

# No matching distribution found: Fehler
#python3-rpi.gpio

ADD /script.py /

# Setzt Python3 vorraus
CMD ["python3" ,"./script.py" ]
