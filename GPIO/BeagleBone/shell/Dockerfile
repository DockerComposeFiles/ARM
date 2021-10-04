FROM arm32v7/debian:buster AS base
RUN apt update && apt -y upgrade
RUN apt install -y nano tree lynx iputils-ping

FROM base AS debug
RUN apt install -y apt-utils i2c-tools

FROM debug AS shell-i2c
ARG environment=shell_htu
COPY script.sh /
RUN chmod +x script.sh
CMD ./script.sh

