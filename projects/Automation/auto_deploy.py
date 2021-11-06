#!/usr/bin/env python
import os
import time

# Skript zum Automatischen Deployen von Anwendungen

# Container maximal einmal starten
bmp180_ = True
bmp280_ = True


# Deploy Funktionen BMP180
def bmp180():
    bmp180_scan = os.system("i2cget -y 1 0x77")
    print(bmp180_scan)
    if bmp180_scan == 0x00 or 77 or 0:
        # print("bmp180 Container will download", flush=True)
        # os.system("docker pull 326567/bmp180")
        print("\nbmp180 Container will deploy", flush=True)
        os.system("docker run --device /dev/i2c-1 326567/bmp180 &")

    elif bmp180_scan == "Error: Read failed\n512":
        print("\nbmp180 no connection by 512", flush=True)

    elif bmp180_scan == "Error: Read failed\n589":
        print("\nbmp180 no connection by 589", flush=True)

    else:
        print("\nbmp180 no connection: unknown message", flush=True)


# Deploy Funktionen BMP280
def bmp280():
    bmp280_scan = os.system("i2cget -y 1 0x76")
    print(bmp280_scan)
    if bmp280_scan == 0x00 or 77 or 0:
        # print("bmp280 Container will download", flush=True)
        # os.system("docker pull 326567/bmp280")
        print("\nbmp280 Container will deploy", flush=True)
        os.system("docker run --device /dev/i2c-1 326567/bmp280 &")

    elif bmp280_scan == "Error: Read failed\n512":
        print("\nbmp180 no connection by 512", flush=True)

    elif bmp280_scan == "Error: Read failed\n588":
        print("\nbmp180 no connection by 588", flush=True)

    else:
        print("\nbmp280 no connection: unknown message", flush=True)


"""
# HTU21D wird nicht erkannt
def htu21d():
    if os.system("i2cget -y 1 0x40"):
        #print("htu21d Container will download", flush=True)
        #os.system("docker pull 326567/htu21d")
        print("htu21d Container will deploy", flush=True)
        os.system("docker run --device /dev/i2c-1 326567/htu21d")
    else:
        print("htu21d no connection", flush=True)
"""

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

    time.sleep(10)
done
