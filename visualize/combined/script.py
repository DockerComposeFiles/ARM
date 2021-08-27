import time

print("reading start")
# Endlosschleife
i = 0
while i <= 1:

    # Daten auslesen
    fo = open('/data/data.txt', 'r')
    for line in fo:
        print(line.rstrip())
    fo.close()
    time.sleep(1)
