FROM arm32v7/python:rc-buster AS debug

# Updaten des Images
RUN apt update && apt upgrade -y
# Debug Programme
RUN apt install nano tree lynx iputils-ping -y

FROM debug AS rpi
# update python
RUN -H pip2 install --upgrade pip
RUN -H pip3 install --upgrade pip
# installiere Bibliotheken
RUN python -m pip install RPi.GPIO
RUN python3 -m pip install RPi.GPIO
# installiere Treiber
RUN apt install -y apt-utils i2c-tools python-smbus -y \
    && apt install rpi.gpio python-rpi.gpio python3-rpi.gpio python-dev -y

# Manuelle Installation
#RUN wget https://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.5.11.tar.gz
#RUN tar -xvf RPi.GPIO-0.5.11.tar.gz
#RUN cd RPi.GPIO-0.5.11
#RUN python setup.py install
#RUN cd ~ && rm -rf RPi.GPIO-0.*
#WORKDIR /

FROM rpi AS lc

# Python Skript des LC-Display ist Lizensiert
# und daher hier nicht verfügbar
COPY script.py /
RUN chmod +x script.py
CMD [ "python", "./script.py" ]
