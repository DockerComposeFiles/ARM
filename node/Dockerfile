FROM arm32v7/node

RUN apt clean
RUN apt update
#RUN apt -y upgrade
RUN apt install -y nano

COPY app.js /
COPY script.sh /

# CMD []