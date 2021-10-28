FROM arm32v7/python:rc-bullseye

# Container auf den neuesten Stand bringen
# Installation von benötigten Paketen
RUN apt update \
    && apt upgrade -y \
    && apt install apt-utils i2c-tools -y \
    && apt clean

# Benötigte Python Bibliotheken
RUN pip3 install smbus2

# BMP280 Bibliothek, Als Adresse ist 76 eingetragen
ADD /bme280.py /
ADD /script.py /

# Vergeben der Berechtigung zum Ausführen des Skriptes hier nicht nötig
#RUN chmod +x script.py && chmod +x bme280.py
CMD ["python3" ,"./script.py" ]
