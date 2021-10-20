FROM arm32v7/debian

RUN apt update && apt upgrade -y
RUN apt install nano -y
RUN apt clean

ENTRYPOINT ["tail", "-f", "/dev/null"]
