FROM arm32v7/python:rc-buster
# Teilweise benötigt
# Verbessert Support
# Benötigt

RUN apt update \
    && apt upgrade -y \
    && apt install apt-utils i2c-tools python-smbus nano -y \
    python3-pip python3 \
    build-essential python-dev -y \
    && apt clean

RUN pip install smbus Adafruit_BBIO
RUN pip3 install --upgrade setuptools adafruit-circuitpython-htu21d

ADD /script.py /
CMD ["python3" ,"./script.py" ]
