FROM arm32v7/node:14

#RUN apt update
#RUN apt -y upgrade
#RUN apt install -y nano

COPY package.json /
COPY server.js /
COPY app.js /

RUN npm install;
CMD ["node", "server.js"]