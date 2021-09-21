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

# konfiguriere I2C PINS
config-pin p9.19 gpio # shared i2c Pin
config-pin p9.20 gpio # shared i2c Pin

# Moeglicherweise alternativen
#config-pin p9.17 gpio # normaler i2c Pin
#config-pin p9.18 gpio # normaler i2c Pin

exit 0