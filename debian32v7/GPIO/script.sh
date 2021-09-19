#!/bin/sh
### Dieses Skript analysiert die GPIO des BeagleBone Black

## GPIO Abfragen
# Abfrage, ob der  OS Kernel GPIO unterstützt
grep GPIOLIB /boot/config-$(uname -r)
echo
grep GPIO_SYSFS /boot/config-$(uname -r)
echo

# I2C Abfragen
# Zeigt installierte BUS Adapter an
echo "installed i2c adapters:"
i2cdetect -l
echo
echo "connected devices:"
# Scannt den I2C Adressbereich und zeigt I2C antworten von Geraeten an
i2cdetect -y 1

## Angeschlossene USB-Geräte anzeigen lassen
lsusb