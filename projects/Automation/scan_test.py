import os

print(os.system("i2cget -V" + "\n"), flush=True)

print(os.system("i2cget -y 1 0x77"), flush=True)
print(os.system("i2cget -y 1 0x76"), flush=True)
print(os.system("i2cget -y 1 0x40"), flush=True)
print("\n", flush=True)

# Konvertierung des Scan Objektes
def object_converter(current_object):
    try:
        obj = int(current_object)
    except:
        obj = 0
    return obj

#Scann des ersten Sensors
obj77 = os.system("i2cget -y 1 0x77")
res77 = object_converter(obj77)

print(77 + res77, flush=True)
