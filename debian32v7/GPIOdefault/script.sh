# Dieses Skript gibt die über i2C erkannten GPIO Geraete aus.

# Zeigt installierte BUS Adapter an
i2cdetect -l
# Scannt den I2C Adressbereich und zeigt I2C antworten an
i2cdetect -y 1