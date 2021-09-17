#!/bin/sh

# Dieses Skript gibt die über GPIO und i2C erkannten GPIO Geraete aus.

# GPIO Abfragen
# Abfrage, ob der  OS Kernel GPIO unterstützt
grep GPIOLIB /boot/config-$(uname -r)
echo
grep GPIO_SYSFS /boot/config-$(uname -r)
echo
# Abfrage, ob pin 7 in "gpio mode" geschaltet ist.
echo 7 > /sys/kernel/debug/omap_mux/gpmc_ad4
echo

# I2C Abfragen
# Zeigt installierte BUS Adapter an
echo "installed i2c adapters:"
i2cdetect -l
echo
echo "connected devices:"
# Scannt den I2C Adressbereich und zeigt I2C antworten von Geraeten an
i2cdetect -y 1
