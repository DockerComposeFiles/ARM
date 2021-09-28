## GPIO
Dieser Ordner enthält Containerdateien, um den Zugriff auf die GPIO zu realisieren.
In den Unterordnern sind verschiedene Methoden für den Zugriff auf die GPIO enthalten.

### i2c
Befehl für die Ausführung des Containers mit dem Zugriff auf die GPIO und i2c mountpoints:

docker run --device /dev/gpiomem --device /dev/i2c-1 -it $(docker build -q .)

## Updaten eines Dockerhub repositorys
docker build . -t 326567/gpio

docker push 326567/gpio

docker pull 326567/gpio

docker run --device /dev/gpiomem --device /dev/i2c-1 -it 326567/gpio

Gerätefreigaben:

      - /dev/mem
      - /dev/gpiomem

      - /dev/i2c-1
      - /dev/i2c-0
      - /dev/i2c/1
      - /dev/i2c/0

      - /dev/gpio
