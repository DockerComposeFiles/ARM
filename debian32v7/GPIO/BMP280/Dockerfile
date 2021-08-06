FROM arm32v7/python:rc-buster
#RUN apt clean
RUN apt update

# Bibliotheken
RUN apt install -y apt-utils i2c-tools python-smbus
#RUN apt install -y python3-smbus

# BMP Bibliothek, Als Adresse ist 76 eingetragen
ADD /bme280.py /
ADD /script.py /script.py

RUN chmod 777 script.py
RUN chmod 777 bme280.py
CMD ["python3" ,"./script.py" ]