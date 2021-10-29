#!/bin/bash
import os
import time

# Skript zum Automatischen Deployen von Anwendungen
# x = chr(os.system("i2cdetect -y 1"))
#

# Container maximal einmal starten
bmp180_ = True
bmp280_ = True
htu21d_ = True


# Deploy Funktionen
# Sensor 1
def bmp180():
    if os.system("i2cget -y 1 0x77"):
        #print("bmp180 Container will download", flush=True)
        #os.system("docker pull 326567/bmp180")
        print("bmp180 Container will deploy", flush=True)
        os.system("docker run --device /dev/i2c-1 326567/bmp180")


# Sensor 2
def bmp280():
    if os.system("i2cget -y 1 0x76"):
        #print("bmp280 Container will download", flush=True)
        #os.system("docker pull 326567/bmp280")
        print("bmp280 Container will deploy", flush=True)
        os.system("docker run --device /dev/i2c-1 326567/bmp280")


# Sensor 3
def htu21d():
    if os.system("i2cget -y 1 0x40"):
        #print("htu21d Container will download", flush=True)
        #os.system("docker pull 326567/htu21d")
        print("htu21d Container will deploy", flush=True)
        os.system("docker run --device /dev/i2c-1 326567/htu21d")


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

    time.sleep(10)
done
