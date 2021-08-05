Die zwei in diesem Ordner vorgestellten GPIO Zugriffsmöglichkeiten
funktionieren mit Docker Swarm nicht.

### Methode 1 - privilegierte Container
docker run --privileged -d privileged_GPIO -it $(docker build -q .)
### Methode 2 - Einbinden des GPIO Gerätes
docker run --device /dev/gpiomem -d deviced_GPIO -it $(docker build -q .)