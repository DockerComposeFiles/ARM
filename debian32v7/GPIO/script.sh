#!/bin/sh
### Dieses Skript analysiert die GPIO des BeagleBone Black

## GPIO Abfragen
# Abfrage, ob der  OS Kernel GPIO unterstützt
grep GPIOLIB /boot/config-$(uname -r)
echo
grep GPIO_SYSFS /boot/config-$(uname -r)
echo
# Abfrage, ob pin 7 in "gpio mode" geschaltet ist.
echo 7 > /sys/kernel/debug/omap_mux/gpmc_ad4
echo

## PIN Abfragen
# Informationen über PINs in Verwendung
/sys/kernel/debug/pinctrl/44e10800.pinmux# cat pingroups

# Information über zugewiesene PINs in verwendung
sys/kernel/debug/pinctrl/44e10800.pinmux# cat pinmux-pins |more

# Liste alles PINs
/sys/kernel/debug/pinctrl/44e10800.pinmux# cat pins |more


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