#!/usr/bin/python
# Einbindung der Python Bibliothek
# Angepasste Form
import bme280


# Hauptschleife


# Messdaten Holen
temperatur, druck, x = bme280.readBME280All()

# Daten in volume schreiben
fo = open('/data/data.txt', 'w')
fo.write(str(temperatur))
fo.write(str(druck))
fo.close()

fa = open('/data/all_data.txt', 'a')
fa.write((str(temperatur)))
fa.write(str(druck))
fa.close()
print("write_finish")

# Ausgabe
#print("Temperatur : ", temperatur, "C")
#print("Druck: ", druck, "hPa")
