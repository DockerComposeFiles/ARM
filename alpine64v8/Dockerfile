FROM arm64v8/alpine:latest

# Ungetestet
#Update Methode funktioniert nicht
#RUN su root apk clean
#RUN apt update
#RUN apk -y upgrade
#RUN apk install -y nano

# Entrypoint ist zusätzlich in docker-compose festgelegt
ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]