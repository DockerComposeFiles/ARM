## Einfaches Einbinden des volume
volumes:
      - /data

## externe Einbindung des volume
docker volume create --name=data
    external: true
