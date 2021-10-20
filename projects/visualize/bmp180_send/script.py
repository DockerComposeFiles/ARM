#!/usr/bin/python
# Einbindung der Python Bibliothek
# Angepasste Form
import os
import time
import bme280

# Löschen vorheriger Daten
os.remove('/data/data.txt')
os.remove('/data/all_data.txt')

# Hauptschleife
i = 0
while i <= 200:
    i = i + 1  # Zu Testzwecken auf die Aufnahme von 200 Werten begrenzt.
    # Messdaten Holen
    temperatur, druck, x = bme280.readBME280All()

    # Daten in volume schreiben
    fo = open('/data/data.txt', 'w')
    fo.write(str(temperatur) + "\r\n")
    fo.write(str(druck) + "\r\n")
    fo.close()

    fa = open('/data/all_data.txt', 'a')
    fa.write(str(temperatur) + "\r\n")
    fa.write(str(druck) + "\r\n")
    fa.close()

    # Warten bis der Controller den nächsten Wert senden kann
    time.sleep(1)

print("write_finish")

# Ausgabe
print("Temperatur : ", temperatur, "C")
print("Druck: ", druck, "hPa")
