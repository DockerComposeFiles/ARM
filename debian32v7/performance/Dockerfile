FROM arm32v7/python:rc-buster

# Aktualisierung der Paketquellen vergrößert Image um c.a. 200 MB
RUN apt update
# Installiert nano, für eine bessere Analyse
RUN apt install nano

# "command line interface" zum testen der Internetgeschwindigkeit
RUN pip install speedtest-cli

# Testdatei zum auslesen
ADD https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt /passwords
# Skript zum testen der Lese- und Schreibleistung.
# ADD https://raw.githubusercontent.com/DockerComposeFiles/ARM/main/debian32v7/performance/speedtest.py ./speedtest.py
COPY ./speedtest.py /speedtest.py

# Aufruf des Internettests mit speedtest-cli
CMD ["speedtest-cli"]

# Ausführung des Skriptes
CMD [ "python", "./speedtest.py" ]

