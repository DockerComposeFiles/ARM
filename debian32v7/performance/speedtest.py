#!/usr/bin/env python

# Auslesen einer Datei
import sys
import time

print("Test start")

# Messen der Lesezeiten
readStart = time.time()

# Testdatei
readFile = "passwords"
# Datei wird in f geöffnet und gelesen
with open(readFile) as f:
    content = f.readlines()
f.close()

# Berechnung der Lesezeiten
readTime = (time.time() - readStart)
print('readTime:')
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
print('writeTime:')
print(writeTime)
# erzwingen der Ausgabe
sys.stdout.flush()

# Container wird für 3 Minuten im Leerlauf gehalten, bevor er stoppt
time.sleep(180)
print("Test end")
