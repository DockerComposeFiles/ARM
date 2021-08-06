Befehl für die Ausführung des Containers:

docker run --device /dev/gpiomem --device /dev/i2c-1 -it $(docker build -q .)

## Updaten des Dockerhub repositorys
docker build . -t 326567/gpio
docker push 326567/gpio
docker pull 326567/gpio
docker run --device /dev/gpiomem --device /dev/i2c-1 -it 326567/gpio

