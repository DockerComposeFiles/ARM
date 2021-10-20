# Setze eine aktuele feste Version
FROM arm32v7/debian

# Aktualisieren
RUN apt update && apt upgrade -y && apt install nano -y
RUN apt clean

# Füge Nutzer mit Nutzerrechten hinzu
RUN useradd 8877 nonroot
# Wechel auf den Nutzer
USER nonroot

# Teste die Umgebung: Aufruf im Nutzerverzeichniss
RUN pwd && ls
