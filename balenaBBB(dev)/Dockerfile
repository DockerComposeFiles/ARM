FROM balenalib/beaglebone-black-debian-python:latest AS base
# Behebt Fehler

# Updaten des Images
RUN apt update && apt -y upgrade
# Debug Programme
RUN apt install -y nano && apt install tree && apt install -y lynx && apt install -y iputils-ping

FROM base AS htu21d

#RUN apt install python3 && apt install python3-pip
RUN pip install adafruit-circuitpython-HTU21D
#RUN pip install --no-cache-dir -r requirements.txt

RUN apt clean
COPY . .

#CMD [ "python", "./your-daemon-or-script.py" ]
CMD ["./script.sh"]