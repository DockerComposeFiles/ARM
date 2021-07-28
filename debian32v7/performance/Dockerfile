FROM arm32v7/python:rc-buster

# Aktualisierung der Paketquellen vergrößert Image um c.a. 200 MB
RUN apt update
# Installiert nano, für eine bessere Analyse
RUN apt install nano

# "command line interface" zum testen der Internetgeschwindigkeit
RUN pip install speedtest-cli

# Testdatei zum auslesen
COPY ./passwords.txt /
# Die Originaldatei ist unter
# https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt /passwords
# zu finden.

# Skript zum testen der Lese- und Schreibleistung.
COPY ./speedtest.py /

# Ausführung des Skriptes
CMD [ "python", "./speedtest.py" ]

# Aufruf des Internettests mit speedtest-cli
CMD ["speedtest-cli"]