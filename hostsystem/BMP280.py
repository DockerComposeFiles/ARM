#!/usr/bin/python
import bme280

#Messdaten Holen
temperatur,druck, x = bme280.readBME280All()
print ("Temperatur : ", temperatur, "C")
print ("Druck: ", druck, "hPa")
