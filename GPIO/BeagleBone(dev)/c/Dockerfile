FROM arm32v7/debian:stable AS base
RUN apt update && apt -y upgrade
RUN apt install -y nano tree lynx iputils-ping

FROM base AS debug
RUN apt install -y apt-utils i2c-tools

FROM debug AS c-i2c
ARG environment=c_htu
RUN apt install -y git && mkdir development && cd development
RUN git clone https://github.com/shabaz123/iobb.git
RUN cd iobb && make && make install

FROM debug AS c-i2c_local
ARG environment=c_local_htu
COPY iofunc/* /
#RUN gcc pin_2.c -iofunc -o main
