#!/bin/sh -e
# turn off LEDs 1 – 3, only 0 will be on
#echo 0 > /sys/class/leds/beaglebone:green:usr1/brightness
#echo 0 > /sys/class/leds/beaglebone:green:usr2/brightness
#echo 0 > /sys/class/leds/beaglebone:green:usr3/brightnes

# configure UART
##config-pin p9.11 uart
##config-pin p9.13 uart

#config-pin p8.37 uart
#config-pin p8.38 uar

# configure P9 GPIO ports
##config-pin p9.12 gpio
##config-pin p9.15 gpio
##config-pin p9.23 gpio
##config-pin p9.27 gpio
##config-pin p9.41 gpio

# configure P8 GPIO ports (nicht nötig)
#config-pin p8.11 gpio
#config-pin p8.12 gpio
#config-pin p8.14 gpio
#config-pin p8.16 gpio
#config-pin p8.18 gpio
#config-pin p8.21 gpio
#config-pin p8.23 gpio
#config-pin p8.25 gpio
#config-pin p8.26 gpio
#config-pin p8.27 gpio
#config-pin p8.28 gpio
#config-pin p8.29 gpio
#config-pin p8.30 gpio
#config-pin p8.31 gpio
#config-pin p8.32 gpio
#config-pin p8.33 gpio
#config-pin p8.34 gpio
#config-pin p8.35 gpio
#config-pin p8.36 gpio
#config-pin p8.39 gpio
#config-pin p8.40 gpio
#config-pin p8.41 gpio
#config-pin p8.42 gpio
#config-pin p8.43 gpio
#config-pin p8.44 gpio
#config-pin p8.45 gpio
#config-pin p8.46 gpi

# configure PWM ports
##config-pin p9.14 pwm
##config-pin p9.16 pwm
##config-pin p9.42 pwm

#config-pin p8.13 pwm
#config-pin p8.19 pw

# configure CAN ports
# P9_19 -> dCAN0 Rx
# P9_20 -> dCAN0 Tx
# P9_24 -> dCAN1 Rx
# P9_26 -> dCAN1 Tx
#config-pin p9.19 can
#config-pin p9.20 can
#config-pin p9.24 can
#config-pin p9.26 ca

#SPI setup
##config-pin p9.28 spi_cs
##config-pin p9.29 spi
##config-pin p9.30 spi
##config-pin p9.31 spi_scl


# konfiguriere HTU21D Pins direkt
##echo 1 > /sys/class/gpio/export
##echo 3 > /sys/class/gpio/export
##echo 19 > /sys/class/gpio/export
##echo 20 > /sys/class/gpio/export

# konfiguriere I2C PINS
#config-pin p9.1 gpio #ground
#config-pin p9.3 gpio #3,3V Power
config-pin p9.17 gpio # normal
config-pin p9.18 gpio # normal

config-pin p9.19 gpio # shared
config-pin p9.20 gpio # shared

# konfiguriere testpin 7 an P8
config-pin p8.17 gpio # shared

exit 0
