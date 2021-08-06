FROM arm32v7/python:rc-buster
#RUN apt clean
RUN apt update

# Bibliotheken
RUN apt install -y apt-utils i2c-tools python3-smbus

# BMP Bibliothek
# Als Adresse ist 76 eingetragen
ADD /bme280.py /
ADD /script.py /
RUN ls
CMD ["python3" ,"/script.py" ]