FROM arm32v7/python

# Skript zum testen der Internetgeschwindigkeit
RUN pip install speedtest-cli

# festlegen des entrypoint - keep alive
ENTRYPOINT ["tail", "-f", "/dev/null"]