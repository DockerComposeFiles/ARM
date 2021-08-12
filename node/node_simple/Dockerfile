FROM arm32v7/node:14
RUN pwd && ls
RUN apt update
#RUN apt -y upgrade
RUN apt install -y nano
RUN npm install;

COPY package.json /
COPY server.js /
COPY app.js /

CMD ["node", "server.js"]