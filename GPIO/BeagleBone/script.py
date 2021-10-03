import os

import Adafruit_BBIO.GPIO as GPIO

# Beispiel
#GPIO.setup("P8_10", GPIO.OUT)
#GPIO.output("P8_10", GPIO.HIGH)

# konfiguriere I2C Pins direkt
GPIO.setup("P9_17", GPIO.IN)
GPIO.setup("P9_18", GPIO.IN)
GPIO.setup("P9_19", GPIO.IN)
GPIO.setup("P9_20", GPIO.IN)
GPIO.setup("P9_21", GPIO.IN)
GPIO.setup("P9_22", GPIO.IN)

GPIO.setup("P9_24", GPIO.IN)
GPIO.setup("P9_22", GPIO.IN)

os.system('i2cdetect -r -y 0')

GPIO.cleanup()
