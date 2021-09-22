## Aufbau der Basis Image Dockerfiles
- Import des basis Images
- Updaten des Paketquellencache, (aktualisierung der installierten Programme)
- Installation von Paketen für eine bessere Analyse
- Festlegen eines Entrypoint,
welcher den Container im aktiven Zustand hält

## Aufbau spezifischer Dockerfiles
- Ersten 3 Punkte des Basis-Images
- Installation spezifischer Bibliotheken
- Hinzufügen Arbeitsdateien und Ausführung dieser

CentOS und Fedora Unterstützen kein Arm 32 bit Paketmanager.