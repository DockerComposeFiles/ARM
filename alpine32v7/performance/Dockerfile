FROM arm32v7/python:rc-alpine

# APK gewährt aufgrund der angepassten Arm-Version kein Zugriff auf die Paketquellen.
# RUN apk update
# RUN apk add --upgrade nano

# "command line interface" zum testen der Internetgeschwindigkeit
RUN pip install speedtest-cli
# Aufruf der Bibliothek mit
RUN speedtest-cli


# Testdatei zum auslesen
ADD https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt /passwords
# Skript zum testen der Lese- und Schreibleistung.
# Ein Lokales hinzufügen der Datei über den ADD oder COPY Befehl schlug Fehl. Deswegen wird die Datei über Github hinzugefügt.
ADD https://raw.githubusercontent.com/DockerComposeFiles/ARM/main/alpine32v7/performance/read_write_speedtest.py /read_write_speedtest.py
COPY ./read_write_speedtest.py /read_write_speedtest.py
#
# Vergeben von Berechtigung
RUN chown root /read_write_speedtest.py
RUN chmod 777 /read_write_speedtest.py
# Ausführung des Skriptes
CMD [ "python", "./read_write_speedtest.py" ]

