FROM arm32v7/python:rc-buster AS debug

# Updaten des Images
RUN apt update && apt upgrade -y
# Debug Programme
RUN apt install nano tree lynx iputils-ping -y

FROM debug AS rpi
# Bibliotheken
RUN apt install -y apt-utils i2c-tools python-smbus -y
RUN apt install rpi.gpio python-rpi.gpio python3-rpi.gpio python-dev -y

# Manuell
#RUN wget https://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.5.11.tar.gz
#RUN tar -xvf RPi.GPIO-0.5.11.tar.gz
#RUN cd RPi.GPIO-0.5.11
#RUN python setup.py install
#RUN cd ~ && rm -rf RPi.GPIO-0.*
#WORKDIR /

FROM rpi AS lc
RUN apt clean

COPY script.py /
RUN chmod +x script.py
CMD [ "python", "./script.py" ]
