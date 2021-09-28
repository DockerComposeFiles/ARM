#!/bin/sh

#echo 48 > /sys/class/gpio/export
#echo 50 > /sys/class/gpio/export
#echo 51 > /sys/class/gpio/export
#echo 60 > /sys/class/gpio/export

config-pin p9.17 gpio # normal
config-pin p9.18 gpio # normal

config-pin p9.19 gpio # shared
config-pin p9.20 gpio # shared

# konfiguriere testpin 7 an P8
config-pin p8.17 gpio # shared

exit 0
