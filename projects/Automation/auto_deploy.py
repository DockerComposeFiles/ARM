#!/usr/bin/env python
import os
import time

# Skript zum Automatischen Deployen von Anwendungen

# Container maximal einmal starten
bmp180_is_started = False
bmp280_is_started = False
htu21d_is_started = False

# Konvertierung des Scan Objektes
def object_converter(current_object):
    try:
        obj = int(current_object)
    except:
        obj = -1
    return obj


# Deploy Funktionen BMP180
def bmp180_start():
    bmp180_scan = os.system("i2cget -y 1 0x77")
    bmp180_int = object_converter(bmp180_scan)
    # print(chr(bmp180_int))

    if bmp180_int == 0:
        # print("bmp180 Container will download", flush=True)
        # os.system("docker pull 326567/bmp180")
        print("BMP180 Container will deploy\n", flush=True)
        os.system("docker run --device /dev/i2c-1 --name=bmp180 -d 326567/bmp180 &")
        return True
    else:
        print("bmp180 no connection\n", flush=True)
        return False

def bmp180_stop():
    bmp180_scan = os.system("i2cget -y 1 0x77")
    bmp180_int = object_converter(bmp180_scan)

    if bmp180_int == 0:
        return True
    else:
        os.system("docker stop bmp180 && docker rm bmp180 &")
        return False

# Deploy Funktionen BMP280
def bmp280_start():
    bmp280_scan = os.system("i2cget -y 1 0x76 \n")
    bmp280_int = (object_converter(bmp280_scan))
    # print("\n" + chr(bmp280_int))

    if bmp280_int == 0:
        # print("bmp280 Container will download", flush=True)
        # os.system("docker pull 326567/bmp280")
        print("BMP280 Container will deploy\n", flush=True)
        os.system("docker run --device /dev/i2c-1 --name=bmp280 -d 326567/bmp280 &")
        return True
    #    elif bmp280_int.__contains__("Error: Read failed"):
    #        print("bmp180 no connection: not connected \n", flush=True)

    else:
        print("bmp280 no connection\n", flush=True)
        return False

def bmp280_stop():
    bmp280_scan = os.system("i2cget -y 1 0x76")
    bmp280_int = object_converter(bmp280_scan)

    if bmp280_int == 0:
        return True
    else:
        os.system("docker stop bmp280 && docker rm bmp280 &")
        return False


# HTU21D wird nicht erkannt
def htu21d_start():

    htu21d_scan = os.system("i2cget -y 1 0x40 \n")
    htu21d_int = (object_converter(htu21d_scan))

    if htu21d_int == 0:
        #print("htu21d Container will download", flush=True)
        #os.system("docker pull 326567/htu21d")
        print("htu21d Container will deploy\n", flush=True)
        os.system("docker run --device /dev/i2c-1 --name=htu21d -d 326567/htu21d &")
        return True
    else:
        print("htu21d no connection\n",flush=True)
        return False

def htu21d_stop():
    htu21d_scan = os.system("i2cget -y 1 0x40")
    htu21d_int = object_converter(htu21d_scan)
    if htu21d_int == 0:
        return True
    else:
        os.system("docker stop htu21d && docker rm htu21d &")
        return False

# Hauptschleife
while True:

    # BMP180 Prüfen
    if not bmp180_is_started:
        bmp180_is_started = bmp180_start()
    else:
        bmp180_is_started = bmp180_stop()
    time.sleep(10)

    # BMP280 Prüfen
    if not bmp280_is_started:
        bmp280_is_started = bmp280_start()
    else:
        bmp280_is_started = bmp280_stop()
    time.sleep(10)

    # htu21d prüfen
    if not htu21d_is_started:
        htu21d_is_started = htu21d_start()
    else:
        htu21d_is_started = htu21d_stop()
    time.sleep(10)
