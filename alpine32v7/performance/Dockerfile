FROM arm32v7/python:rc-alpine

# Pakete stehen nicht zur Verfügung - apk auf beagle versuchen
# RUN apk update
# RUN apk add --upgrade nano

# "command line interface" zum testen der Internetgeschwindigkeit
# Aufruf mit: speedtest-cli
RUN pip install speedtest-cli
RUN speedtest-cli

# Testdatei zum auslesen
ADD https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt /passwords
# Skript zum testen der Lese- und Schreibleistung
ADD https://raw.githubusercontent.com/DockerComposeFiles/ARM/main/debian32v7/performance/read_write_speedtest.py ./read_write_speedtest.py
# Vergeben von Berechtigung
RUN chown root /read_write_speedtest.py
RUN chmod 777 /read_write_speedtest.py
# Ausführung des Skriptes
CMD [ "python", "./read_write_speedtest.py" ]

