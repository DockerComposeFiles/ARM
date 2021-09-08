## Einfaches Einbinden
volumes:
      - /data

## external ?
docker volume create --name=data
    external: true


# Network
docker network create macvlan0

docker network create --gateway 172.24.0.1 --subnet 172.24.0.0/24 macvlan0
docker network rm macvlan0
