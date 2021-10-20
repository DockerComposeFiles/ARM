import time
from pathlib import Path

print("reading start", flush=True)

# Wenn Datei nicht existiert, ist der Sensor_Container noch nicht Einsatzbereit
# Warten, dass Sensor_Container mit dem schreiben begonnen hat
fileName = r"/data/data.txt"
fileObj = Path(fileName)
while not fileObj.is_file:
    print("no_File", flush=True)
    time.sleep(5)
if fileObj.is_file:
    print("file exist: " + str(fileObj) + "->Objekt , Name<-" + fileName, flush=True)

# Einlesen der Daten (in einer Endlosschleife)
i = 0
while i <= 20:
    # Zu Testzwecken wird nach 200 Werten Abgebrochen
    i = i + 1
    print(i, flush=True)
    # Auslesen der Daten
    try:
        # Einlesen des letzten Wertes
        fo = open('/data/data.txt', 'r')
        for line in fo:
            print(line.rstrip(), flush=True)
        fo.close()

        # Einlesen aller Werte
        fa = open('/data/all_data.txt', 'r')
        for line in fa:
            print("all:" + line, flush=True)
        fa.close()

        # Warten bis der Controller den nächsten Wert senden kann
        time.sleep(1)
    except:
        print("exception: no file", flush=True)
        time.sleep(3)

quit()
