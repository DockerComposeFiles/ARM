#!/usr/bin/env python

# Auslesen einer Datei
import sys
import time

filename = "passwords"

# Datei wird als f geöffnet und gelesen
with open(filename) as f:
    content = f.readlines()

# Schreiben des Inhalts in eine Datei
o = open('passwords_output', 'w')
for line in content:
    o.write(line)
o.close()

