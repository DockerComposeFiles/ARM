FROM arm32v7/python:rc-buster

# Aktualisierung der Paketquellen
RUN apt update
# Installiert nano, für eine bessere Analyse
RUN apt install nano

# "command line interface" zum testen der Internetgeschwindigkeit
RUN pip install speedtest-cli

# Testdatei zum auslesen
# Die Originaldatei ist unter
# https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
# zu finden.
COPY passwords.txt /passwords.txt

# Skript zum testen der Lese- und Schreibleistung.
COPY speedtest.py /speedtest.py

# Ausführung der Skripte
ADD start.sh /
RUN chmod +x /start.sh

# Ausführen der Skripte
CMD ["/start.sh"]

