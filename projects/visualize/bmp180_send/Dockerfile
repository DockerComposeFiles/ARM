FROM arm32v7/python:rc-buster
#RUN apt clean
RUN apt update

# Bibliotheken
RUN apt install -y apt-utils i2c-tools python-smbus
RUN pip3 install smbus
#RUN apt install -y python3-smbus

# BMP Bibliothek, Als Adresse ist 76 eingetragen
ADD /bme280.py /
ADD /script.py /

# Vergeben der Berechtigung zum Ausführen des Skriptes
#RUN chmod +x script.py && chmod +x bme280.py
CMD ["python3" ,"./script.py" ]
