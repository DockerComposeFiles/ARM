# py_backend_1
Dieser Container liest die BMP Daten aus dem volume und sendet sie dem stout.

## Einfaches Einbinden des volume
volumes:
      - /data

## externe Einbindung des volume
docker volume create --name=data
    external: true
