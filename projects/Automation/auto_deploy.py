#!/bin/bash
import os
import time

# Nur einmal Container starten
bmp180_ = True
bmp280_ = True
htu21d_ = True


# Deploy Funktionen
# Wenn Sensor 1
def bmp180():
    x = os.system("i2cdetect -y 1")
    if x.contains("77"):
        os.system("docker run --device /dev/i2c-1 myimage")
    print("bmp180 Container will deploy", flush=True)

    # Wenn Sensor 2


def bmp280():
    x = os.system("i2cdetect -y 1")
    if x.contains("76"):
        os.system("docker run --device /dev/i2c-1 myimage")
    print("bmp280 Container will deploy", flush=True)

    # Wenn Sensor 3


def htu21d():
    x = os.system("i2cdetect -y 1")
    if x.contains("40"):
        os.system("docker run --device /dev/i2c-1 myimage")
        print("htu21d Container will deploy", flush=True)


# Hauptschleife
while True:

    # Sensor 1
    if bmp180_:
        bmp180_ = False
        bmp180()

    # Sensor 2
    time.sleep(.3)
    if bmp280_:
        bmp280_ = False
        bmp280()

    # Sensor 3
    time.sleep(.3)
    if htu21d_:
        htu21d_ = False
        htu21d()

done
