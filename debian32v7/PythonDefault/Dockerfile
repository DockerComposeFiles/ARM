FROM arm32v7/python:rc-buster

RUN apt clean
RUN apt update
RUN apt upgrade
RUN apt install -y nano

# Standard Entrypoint
ENTRYPOINT ["/bin/sh", "-c"]