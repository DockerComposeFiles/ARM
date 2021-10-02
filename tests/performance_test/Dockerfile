FROM arm32v7/python:rc-buster

# Testdatei zum auslesen - online
#ADD https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt /passwords
# Lokal
COPY /passwords.txt /

# Skript zum testen der Lese- und Schreibleistung - online
#ADD https://raw.githubusercontent.com/DockerComposeFiles/ARM/main/alpine32v7/performance/read_write_speedtest.py /read_write_speedtest.py
# Lokal
COPY ./read_write_test_v2.py /

# Berechtigungen
RUN chmod +x ./passwords.txt && chmod +x ./read_write_test_v2.py
# Ausführung des Skriptes
CMD [ "python", "./read_write_test_v2.py" ]
