#!/usr/bin/python
# Einbindung der Python Bibliothek
# Angepasste Form
import bme280

# Messdaten Holen
temperatur, druck, x = bme280.readBME280All()

# Daten in volume schreiben
fo = open('/data/data.txt', 'w')
fo.write(str(temperatur))
fo.write(str(druck))
fo.close()
print("write_finish")

# Ausgabe
#print("Temperatur : ", temperatur, "C")
#print("Druck: ", druck, "hPa")
