## Build Kontext

Dieser Ordner zeigt, wie Dateien dem Build-Kontext hinzugefügt werden
und wie sie davon ausgeschlossen werden.

Dateien und Ordner können mittels
.dockerignore
aus dem Build-Kontext ausgeschlossen werden.
Der Build Kontext beschreibt eine virtuell auf das Dateisystem gelegte
Read-Only Schicht, welche bei Änderungen der darunterliegenden Schicht
neu erstellt werden muss.

## Ausgabe:
.

./.dockerignore

./Dockerfile

./add_me.txt

