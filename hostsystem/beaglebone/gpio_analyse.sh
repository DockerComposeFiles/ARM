#!/bin/sh
### Dieses Skript analysiert die GPIO des BeagleBone Black

## GPIO Abfragen
# Abfrage, ob der  OS Kernel GPIO unterstützt
echo "Kernel GPIO:"
grep GPIOLIB /boot/config-$(uname -r)
grep GPIO_SYSFS /boot/config-$(uname -r)
echo
# Abfrage der erkannten GPIO
ls -al /sys/class/gpio
echo

# Abfrage, ob bestimmte pin in "gpio mode" geschaltet ist.
#echo "ask single Pin 4 and 17 of gpio-mode:"
#echo 4 > /sys/kernel/debug/omap_mux/gpmc_ad4
#echo 17 > /sys/kernel/debug/omap_mux/gpmc_ad4
#echo

## PIN Abfragen
# Abfragen uber Debug Informationen
echo "debug:"
cat /sys/kernel/debug/pinctrl/pinctrl-devices
echo
cat /sys/kernel/debug/pinctrl/44e3e000.rtc/pins |more
cat /sys/kernel/debug/pinctrl/44e3e000.rtc/pingroups |more
echo
cat /sys/kernel/debug/pinctrl/44e3e000.rtc/pinconf-config |more

## I2C Abfragen
# Zeigt installierte BUS Adapter an
echo "installed i2c adapters:"
i2cdetect -l
echo
echo "connected devices:"
# Scannt den I2C Adressbereich und zeigt I2C antworten von Geraeten an
i2cdetect -y 1
echo
## Angeschlossene USB-Geräte anzeigen lassen
lsusb