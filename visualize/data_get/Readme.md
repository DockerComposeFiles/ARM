# data_get
Dieser Container liest die Daten des BMP280 volumes aus
und sendet das Ergebnis an den stdin.

## Einfaches Einbinden des volume
volumes:
      - /data

## externe Einbindung des volume
docker volume create --name=data
    external: true
