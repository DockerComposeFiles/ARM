FROM arm32v7/python:rc-buster
RUN apt clean
RUN apt update

# Bibliotheken
RUN apt install -y i2c-tools python3-smbus
# Shellskript zum erfassen angeschlossener Geräte
CMD script.sh