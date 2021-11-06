import os


# Konvertierung des Scan Objektes
def object_converter(current_object):
    try:
        obj = int(current_object)
    except:
        obj = 0
    return obj


# Vergleich
print(os.system("i2cget -V"), flush=True)
print("\n", flush=True)
print(os.system("i2cget -y 1 0x77"), flush=True)
print(os.system("i2cget -y 1 0x76"), flush=True)
print(os.system("i2cget -y 1 0x40"), flush=True)
print("\n", flush=True)

# Scann des 1 Sensors
obj77 = os.system("i2cget -y 1 0x77")
res77 = object_converter(obj77)
print(77 + res77, flush=True)

# Scann des 1 Sensors
obj76 = os.system("i2cget -y 1 0x76")
res76 = object_converter(obj76)
print(76 + res76, flush=True)

# Scann des 3 Sensors
obj40 = os.system("i2cget -y 1 0x40")
res40 = object_converter(obj40)
print(40 + res40, flush=True)
