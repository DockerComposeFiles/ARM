FROM arm32v7/alpine:latest

#Update Methode funktioniert nicht

RUN apk update
RUN apk -y upgrade
RUN apk install -y nano
#RUN su root apk clean

# Entrypoint ist zusätzlich in docker-compose festgelegt
ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]