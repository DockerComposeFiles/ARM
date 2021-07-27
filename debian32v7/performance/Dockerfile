FROM arm32v7/python:rc-buster

# installiere nano, für eine bessere Analyse
RUN apt update
RUN apt-get install nano

# "command line interface" zum testen der Internetgeschwindigkeit
# Aufruf mit: speedtest-cli
RUN pip install speedtest-cli
RUN speedtest-cli

# Testdatei zum auslesen
ADD https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt /passwords
# Skript zum testen der Lese- und Schreibleistung
ADD https://raw.githubusercontent.com/DockerComposeFiles/ARM/main/debian32v7/performance/read_write_speedtest2.py ./read_write_speedtest2.py
# Vergeben von Berechtigung
RUN chown root /read_write_speedtest2.py
RUN chmod 777 /read_write_speedtest2.py
# Ausführung des Skriptes
CMD [ "python", "./read_write_speedtest2.py" ]

