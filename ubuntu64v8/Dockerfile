FROM arm64v8/ubuntu

# Update aller Pakete
#RUN apt clean && apt update && apt upgrade

# Installiert nano, für eine bessere Analyse
RUN apt-get update && apt-get install nano

# festlegen des entrypoint, um den Container dauerhaft laufen zu lassen. Funktion gibt folgenden fehler zurück:
# „tail: cannot read realtime clock: Operation not permitted”
#ENTRYPOINT ["tail", "-f", "/dev/null"]
