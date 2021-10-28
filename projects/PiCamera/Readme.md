## de
Dieser Container demonstriert die Nutzung der Raspberry Pi Kamera.
Um ihn zu nutzen, muss Docker den Zugriff auf die Kamera gegeben werden.
Wenn euer Nutzername pi ist, dann sind diese Eintragungen notwendig:

> sudo usermod -a -G video pi

Das Image MUSS auf einem Raspberry Pi kompiliert werden,
um die "picamera" Bibliothek installieren zu können.

Der picamera Quellcode wurde mittels SPC direkt an den Raspberry übertragen
und befindet sich daher nicht im Repository.


## en
With this container, you would be able to access the Raspberry Pi camera.

### Treiber
Online neueste Programmversion

https://github.com/waveform80/picamera/archive/refs/tags/release-1.13.zip

# Systemvariable, um die Prüfung des System auf PI-OS zu deaktivieren
# war nicht erfolgreich.
> RUN export READTHEDOCS=True

# Befehl, um den Container ohne compose Datei zu starten.

> docker run 326567/raspi-cam-default -p 344:80 -v /opt/vc:/opt/vc --env LD_LIBRARY_PATH=/opt/vc/lib
