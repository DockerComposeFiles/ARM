#!/usr/bin/env python

import pigpio

pigpio.exceptions = False  # Fehlerbehandlung

pi = pigpio.pi()

for bus in range(2):
    for x in range(0x08, 0x79):
        h = pi.i2c_open(bus, x)
        if h >= 0:
            s = pi.i2c_read_byte(h)
            if s >= 0:
                print("device {} found on bus {}".format(x, bus))
            pi.i2c_close(h)

pi.stop()
