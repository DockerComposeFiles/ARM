FROM arm32v7/debian

RUN apt clean
RUN apt update
#RUN apt -y upgrade
RUN apt install -y nano

# Standard Entrypoint
ENTRYPOINT ["/bin/sh", "-c"]