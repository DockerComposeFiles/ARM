#!/usr/bin/python
import time
import board
from adafruit_htu21d import HTU21D

# Erstellt ein Sensor Objekt, um den I2C standard bus zu kommunizieren.
i2c = board.I2C()  # Nutzt board.SCL und board.SDA
sensor = HTU21D(i2c)


while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    time.sleep(2)
