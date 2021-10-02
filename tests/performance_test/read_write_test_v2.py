#!/usr/bin/env python

# Auslesen einer Datei
import sys
import time

print("access-Test start")

# Messen der Lesezeiten
readStart = time.time()

# Testdatei
readFile = "passwords.txt"
# Datei wird in f geoeffnet und gelesen
with open(readFile) as f:
    content = f.readlines()
f.close()

# Berechnung der Lesezeiten
readTime = (time.time() - readStart)
print("readTime:")
print(readTime)
# erzwingen der Ausgabe
sys.stdout.flush()

# Messen der Schreibzeiten
writeStart = time.time()

# Schreiben des Inhalts in eine Datei
o = open('passwords_output', 'w')
for line in content:
    o.write(line)
o.close()

# Berechnung der Schreibzeiten
writeTime = (time.time() - writeStart)
print("writeTime bevor flush:")
print(writeTime)

# erzwingen der Ausgabe
sys.stdout.flush()

# Erneute Berechnung der Schreibzeit
print("writeTime after flush:")
writeTime = (time.time() - writeStart)
print(writeTime)
print("access-Test end")

# container bleibt für Debug-Zwecke fuer weitere drei minuten in Betrieb
time.sleep(180)
