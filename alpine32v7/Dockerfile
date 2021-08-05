FROM arm32v7/alpine:latest

#Update Methode funktioniert nicht
#RUN su root apk clean
#RUN apt update
#RUN apk upgrade
#RUN apk install nano

# Entrypoint ist zusätzlich in docker-compose festgelegt
ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]