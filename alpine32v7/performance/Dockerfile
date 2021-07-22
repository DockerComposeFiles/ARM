FROM arm32v7/python

# installiere nano, für eine bessere Analyse
RUN apk update
RUN apk add --upgrade nano

# "command line interface" zum testen der Internetgeschwindigkeit
# Aufruf mit: speedtest-cli
RUN pip install speedtest-cli
ADD https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt /passwords

# Skript zum testen der Lese- und Schreibleistung
CMD [ "python", "./read_write_speedtest.py" ]
# festlegen des entrypoint - keep alive
ENTRYPOINT ["tail", "-f", "/dev/null"]