FROM arm32v7/debian

# installiere nano, für eine bessere Analyse
RUN apt update
RUN apt install nano

# festlegen des entrypoint, um den Container endlos laufen zu lassen
# ENTRYPOINT ["tail", "-f", "/dev/null"]