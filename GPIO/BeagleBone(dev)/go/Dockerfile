FROM arm32v7/golang:rc-buster AS go-base
RUN apt update && apt -y upgrade
RUN apt install -y nano tree lynx iputils-ping

FROM go-base AS go-debug
RUN apt install -y apt-utils i2c-tools

FROM go-debug AS go-i2c
ARG environment=go_htu
# TODO go-bib for ctrl
# TODO go-lib blink
