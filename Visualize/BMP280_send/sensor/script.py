#!/usr/bin/python
# Einbindung der Python Bibliothek
# Angepasste Form
import bme280

# Messdaten Holen
temperatur, druck, x = bme280.readBME280All()

# Daten in volume schreiben
fo = open('/data/data.txt', 'w')
fo.write(temperatur)
fo.write(druck)
fo.close()
print("finish")

# Ausgabe kommt dann weg
print("Temperatur : ", temperatur, "C")
print("Druck: ", druck, "hPa")
