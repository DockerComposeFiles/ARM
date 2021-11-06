#!/usr/bin/env python
import os
import time

# Skript zum Automatischen Deployen von Anwendungen

# Container maximal einmal starten
bmp180_ = True
bmp280_ = True


# Konvertierung des Scan Objektes
def object_converter(current_object):
    try:
        obj = int(current_object)
    except:
        obj = -1
    return obj


# Deploy Funktionen BMP180
def bmp180():
    bmp180_scan = os.system("i2cget -y 1 0x77")
    bmp180_int = object_converter(bmp180_scan)
    #print(chr(bmp180_int))

    if bmp180_int == 1:
        # print("bmp180 Container will download", flush=True)
        # os.system("docker pull 326567/bmp180")
        print("BMP180 Container will deploy\n", flush=True)
        os.system("docker run --device /dev/i2c-1 326567/bmp180 &")

    else:
        print("bmp180 no connection\n", flush=True)


# Deploy Funktionen BMP280
def bmp280():
    bmp280_scan = os.system("i2cget -y 1 0x76 \n")
    bmp280_int = (object_converter(bmp280_scan))
    #print("\n" + chr(bmp280_int))

    if bmp280_int == 0:
        # print("bmp280 Container will download", flush=True)
        # os.system("docker pull 326567/bmp280")
        print("BMP280 Container will deploy\n", flush=True)
        os.system("docker run --device /dev/i2c-1 326567/bmp280 &")

    #    elif bmp280_int.__contains__("Error: Read failed"):
    #        print("bmp180 no connection: not connected \n", flush=True)

    else:
        print("bmp280 no connection\n", flush=True)


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
