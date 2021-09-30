# Visualise
Dieses Projekt beschäftigt sich mit dem Darstellen der Sensordaten auf einer Weboberfläche.

## Spezifische Compose Datei
Der Ordner besitzt Compose Dateien mit spezifischem Namen.

- docker-compose_volume ist für die Verbindung des BMP- und Backend Container zuständig
- docker-compose_socket ist für die Verbindung des Backend- und Visualizer Container zuständig

Sie können mittels dieser Syntax gebaut / ausgeführt werden:

docker-compose -f {compose file name} build / up
