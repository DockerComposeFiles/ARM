FROM arm32v7/debian

RUN apt clean
RUN apt update
RUN apt upgrade
RUN apt install nano

ENTRYPOINT ["tail", "-f", "/dev/null"]