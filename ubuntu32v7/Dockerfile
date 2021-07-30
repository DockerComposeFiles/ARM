FROM arm32v7/ubuntu

# Update aller Pakete
RUN apt update && apt upgrade

# Installiert nano, für eine bessere Analyse
RUN apt install nano

# festlegen des entrypoint, um den Container dauerhaft laufen zu lassen. Funktion gibt folgenden fehler zurück:
# „tail: cannot read realtime clock: Operation not permitted”
#ENTRYPOINT ["tail", "-f", "/dev/null"]