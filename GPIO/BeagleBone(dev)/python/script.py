import os
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_I2C import Adafruit_I2C

i2c = Adafruit_I2C(0x77)
# konfiguriere 2 - shared I2C PINS
GPIO.setup("P9_19", GPIO.IN)
GPIO.setup("P9_20", GPIO.IN)

# konfiguriere 2 - I2C PINS
GPIO.setup("P9_21", GPIO.IN)
GPIO.setup("P9_22", GPIO.IN)

GPIO.cleanup()


# Prüfen der GPIO
os.system('i2cdetect -r -y 0')
os.system('i2cdetect -r -y 1')
os.system('i2cdetect -r -y 2')
# Python Code

# Löschen der Konfiguration
GPIO.cleanup()
