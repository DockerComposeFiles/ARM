FROM arm32v7/python:rc-buster

# Aktualisierung der Paketquellen
# Installiert nano, für eine bessere Analyse
RUN apt update \
    && apt install nano -y \
    && apt clean \

# "command line interface" zum testen der Internetgeschwindigkeit
RUN pip install speedtest-cli && pip3 install speedtest-cli

# Vergeben von Ausführungsberechtigung
#RUN chown root /read_write_speedtest.py
#RUN chmod 777 /read_write_speedtest.py
#RUN chmod +x speedtest-cli

# Ausführen des CLI
RUN speedtest-cli
