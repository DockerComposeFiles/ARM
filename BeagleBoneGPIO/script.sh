#!/bin/sh
## HTU21D

# konfiguriere 2 - shared I2C PINS
config-pin p9.19 gpio
config-pin p9.20 gpio

# konfiguriere 2 - I2C PINS
config-pin p9.21 gpio
config-pin p9.22 gpio

# # konfiguriere horizontale 1 - I2C PINS
config-pin p9.24 gpio
config-pin p9.26 gpio

# konfiguriere I2C Pins direkt
#echo 17 > /sys/class/gpio/export
#echo 18 > /sys/class/gpio/export
#echo 19 > /sys/class/gpio/export
#echo 20 > /sys/class/gpio/export
#echo 21 > /sys/class/gpio/export
#echo 22 > /sys/class/gpio/export

i2cdetect -l
i2cdetect -r -y 0

exit 0
