#!/usr/bin/env python
import os


# Konvertierung des Scan Objektes
def object_converter(current_object):
    try:
        obj = int(current_object)
    except:
        obj = 0
    return obj


# Vergleich
print(os.system("i2cget -V"), flush=True)
print("\n", flush=True)
# Einfache Ausgabe
print(os.system("i2cget -y 1 0x77"), flush=True)
print(os.system("i2cget -y 1 0x76"), flush=True)
print(os.system("i2cget -y 1 0x40"), flush=True)
print("\n", flush=True)

# Funktion zru Ausgabe
# BMP180 erkennen
obj77 = os.system("i2cget -y 1 0x77 0x00")
res77 = object_converter(obj77)
print(77 + res77, flush=True)
# Ergebnis bei Fehler: 589

# BMP280 erkennen
obj76 = os.system("i2cget -y 1 0x76 0x00")
res76 = object_converter(obj76)
print(76 + res76, flush=True)
# Ergebnis bei Fehler: 588

# HTU21D wird nicht erkannt
obj40 = os.system("i2cget -y 1 0x40 0x00")
res40 = object_converter(obj40)
print(40 + res40, flush=True)
# Ergebnis: 552
print("\n", flush=True)

# Alle Scannen
""""
print("scan all", flush=True)
i = 2
while i < 77:
    i = i + 1
    all_obj = os.system("i2cget -y 1 0x" + str(i))
    res = object_converter(all_obj)
    #    print(os.system("i2cget -y 1 0x" + i), flush=True)
    print(all_obj + i)
"""
