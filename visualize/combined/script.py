import time
from pathlib import Path

print("reading start")

# Wenn Datei nicht existiert, ist der Sensor_Container noch nicht Einsatzbereit
fileName = r"/data/data.txt"
fileObj = Path(fileName)
# Warten auf anderen Container

while not fileObj.is_file:
    time.sleep(5)

# Endlosschleife
i = 0
while i <= 1:

    # Daten auslesen
    fo = open('/data/data.txt', 'r')
    for line in fo:
        print(line.rstrip())
    fo.close()
    time.sleep(1)
