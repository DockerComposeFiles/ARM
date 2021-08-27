import time
from pathlib import Path

print("reading start")

# Wenn Datei nicht existiert, ist der Sensor_Container noch nicht Einsatzbereit
# Warten, dass Sensor_Container mit dem schreiben begonnen hat
fileName = r"/data/data.txt"
fileObj = Path(fileName)
while not fileObj.is_file:
    print("no_File")
    time.sleep(5)
if fileObj.is_file:
    print("file exist:" + str(fileObj) + "-Objekt , Name-" + fileName)

# Einlesen der Daten in einer Endlosschleife
i = 1
while i <= 10:
    i = i + 1
    print("Main Routine")
    # Daten auslesen

    try:
        fo = open('/data/data.txt', 'r')
        for line in fo:
            print(line.rstrip())
        fo.close()
        time.sleep(1)
    except:
        print("exception: no file")
        time.sleep(3)


