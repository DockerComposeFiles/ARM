FROM arm32v7/python:rc-buster

# Container auf den neuesten Stand bringen
# Installation von benötigten und optionalen Paketen
RUN apt update \
    && apt upgrade -y \
    && apt install apt-utils i2c-tools python-smbus nano \
    python3-pip python3 \
    build-essential python-dev -y \
    && apt clean

# Benötigte Python Bibliotheken
RUN pip install smbus Adafruit_BBIO
RUN pip3 install --upgrade setuptools adafruit-circuitpython-htu21d

ADD /script.py /
CMD ["python3" ,"./script.py" ]
