FROM arm32v7/python:rc-buster

# installiere nano, für eine bessere Analyse
RUN apt update
RUN apt-get install nano

# "command line interface" zum testen der Internetgeschwindigkeit
# Aufruf mit: speedtest-cli
RUN pip install speedtest-cli

# Skript zum testen der Lese- und Schreibleistung
ADD https://raw.githubusercontent.com/DockerComposeFiles/ARM/main/debian32v7/performance/read_write_speedtest.py ./read_write_speedtest.py
# Testdatei
ADD https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt /passwords
# Ausführung des Skriptes
CMD [ "python", "./read_write_speedtest.py" ]
# festlegen des entrypoint - keep alive
ENTRYPOINT ["tail", "-f", "/dev/null"]