# Deutsch
Dieses Repository enthält Dockerfiles und Compose Dateien zum Ausführen von Containern auf Hardware der Arm-Architektur.
Mit (dev) gekennzeichnete Ordner beinhalten keine lauffähigen Versionen.

## Setup
Auf dem raspberry Pi muss Docker durch das Convenience Skript installiert werden. Die Dokumentation befindet sich unter:

https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script

Die Docker API sollte mit Benutzerrechten angesprochen werden. Füge darum dein Benutzer der Docker Gruppe hinzu:

usermod -aG docker pi

## Images bauen
"Docker build" sollte auf einem Arm-Gerät ausgeführt werden, um Fehler vorzubeugen.

---

# English
This repository contains dockerfiles and compose files to run arm container

## Docker setup
On raspberry docker must be installed by convenience script. Use this documentation.

https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script

### commands
curl -fsSL https://get.docker.com -o get-docker.sh

sh ./get-docker.sh


don't forget to add pi to the docker group:

usermod -aG docker pi



