## Aufbau der Basis Image Dockerfiles
- Import des basis Images
- (Reinigen, updaten des Paketquellencache,
aktualisierung der Programme)
- Installation von nano für eine bessere Analyse
- Festlegen eines Entrypoint,
welcher den Container bei der Ausführung hält

## Aufbau spezifischer Dockerfiles
- Ersten 3 Punkte des Basis-Images
- Installation spezifischer Bibliotheken
- Hinzufügen Arbeitsdateien und Ausführung dieser

CentOS und Fedora Unterstützen kein Arm 32bit Paketmanager.

Raspberry und BeagleBone Black können nur v7 Container ausführen.

