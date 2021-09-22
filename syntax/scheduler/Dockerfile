# Docker empfihlt pro Container nur eine Anwendung auszuführen.
# Folgend zwei Möglichkeiten, mehrere Prozesse im Container auszuführen

# 1. Starten durch ein shell oder python skript
ADD start.sh /
RUN chmod +x ./start.sh
CMD ["./start.sh"]


# 2. Programm zum starten und verwalten mehrerer Prozesse
RUN apt install -y supervisor

