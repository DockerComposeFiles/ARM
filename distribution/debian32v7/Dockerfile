FROM arm32v7/debian

RUN apt update
# RUN apt -y upgrade
RUN apt install -y nano
RUN apt clean

# Standard Entrypoint
ENTRYPOINT ["/bin/sh", "-c"]