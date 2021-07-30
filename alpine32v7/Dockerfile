# einfaches Baseimage
FROM arm32v7/alpine:latest

# update methode funktioniert nicht
#RUN su root apk update
#RUN apk upgrade

# Hinzufügen eines Entrypoints
RUN apk add --no-cache bash
# festlegen des entrypoint
ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]