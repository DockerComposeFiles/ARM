FROM arm32v7/alpine:latest

#Update Methode funktioniert nicht
RUN su root apk clean
RUN apt update
RUN apk -y upgrade
RUN apk install -y nano
#RUN apk clean

# Entrypoint ist zusätzlich in docker-compose festgelegt
ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]