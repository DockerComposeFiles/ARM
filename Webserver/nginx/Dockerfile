FROM arm32v7/nginx

RUN apt clean
RUN apt update
#RUN apt -y upgrade
RUN apt install -y nano

COPY index.html /
