FROM balenalib/beaglebone-black-debian-python:latest AS base
# Behebt Fehler
RUN apt clean
# Updaten des Images
RUN apt update && apt -y upgrade
# Debug Programme
RUN apt install -y nano && apt install tree && apt install -y lynx && apt install -y iputils-ping

FROM base AS htu21d

#TODO htu bib

#WORKDIR /usr/src/app
COPY script.sh ./
#RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD [ "python", "./your-daemon-or-script.py" ]
CMD ["./script.sh"]