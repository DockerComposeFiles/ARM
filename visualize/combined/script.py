import time

print("reading start")
# Endlosschleife
i = 1
while i <= 0:

    # Daten auslesen
    fo = open('/data/data.txt', 'r')
    for line in fo:
        print(line.rstrip())
    fo.close()
    time.sleep(1)
