fo = open('/data/my_file.txt', 'r')
for line in fo:
    print(line.rstrip())
fo.close()

print("finish")
