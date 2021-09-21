#!/bin/sh -e
## HTU21D
# konfiguriere I2C Pins direkt
#echo 1 > /sys/class/gpio/export
#echo 3 > /sys/class/gpio/export
#echo 19 > /sys/class/gpio/export
#echo 20 > /sys/class/gpio/export

# Anschlüsse
# p9.1 gpio # Ground
# p9.3 gpio # 3,3V Power

# konfiguriere 1 - I2C PINS (funktioniert nicht)
#config-pin p9.17 gpio
#config-pin p9.18 gpio

# konfiguriere 2 - shared I2C PINS
config-pin p9.19 gpio
config-pin p9.20 gpio

# konfiguriere 2 - I2C PINS
config-pin p9.21 gpio
config-pin p9.22 gpio

# # konfiguriere horizontale 1 - I2C PINS
config-pin p9.24 gpio
config-pin p9.26 gpio

exit 0
