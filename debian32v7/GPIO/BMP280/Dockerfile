FROM arm32v7/python:rc-buster
#RUN apt clean
RUN apt update

# Bibliotheken
RUN apt install -y apt-utils i2c-tools python-smbus

# BMP Bibliothek
# Als Adresse ist 76 eingetragen
ADD /bme280.py /
ADD /script.py /script.py
CMD ["python3" ,"./script.py" ]