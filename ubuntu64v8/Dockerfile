FROM arm64v8/ubuntu

#RUN apt clean && apt update && apt upgrade
RUN apt update && apt install nano

# Festlegen des entrypoint, um den Container dauerhaft laufen zu lassen. Funktion gibt folgenden Fehler zurück:
# „tail: cannot read realtime clock: Operation not permitted”
#ENTRYPOINT ["tail", "-f", "/dev/null"]
