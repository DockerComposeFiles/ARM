#!/bin/sh
# Dieses Skript gibt die über i2C erkannten GPIO Geraete aus.

# Zeigt installierte BUS Adapter an
echo "installed i2c adapters:"
i2cdetect -l
echo
echo "connected devices:"
# Scannt den I2C Adressbereich und zeigt I2C antworten an
i2cdetect -y 1

