#!/usr/bin/env python

# Auslesen einer Datei
import sys
import time

filename = "passwords"

# Datei wird als f geöffnet und gelesen
with open(filename) as f:
    content = f.readlines()

# Ausgabe jeder einzelnen Zeile
# We added the comma to print single newlines and not double newlines.
# This is because the lines contain the newline character '\n'.
for line in content:
    print(line), \
sys.stdout.flush()

# erzwingen der Ausgabe

# Schreiben einer Datei