import os
import Adafruit_BBIO.GPIO as GPIO

# Prüfen der GPIO
os.system('i2cdetect -r -y 0')

# Löschen der Konfiguration
GPIO.cleanup()
