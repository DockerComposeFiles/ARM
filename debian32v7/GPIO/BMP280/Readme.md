Befehl für die Ausführung des Containers:

docker run --device /dev/gpiomem --device /dev/i2c-1 -it $(docker build -q .)

