FROM arm32v7/python:rc-buster

RUN apt clean
RUN apt update
#RUN apt -y upgrade
RUN apt install -y nano

ENTRYPOINT ["tail", "-f", "/dev/null"]
