FROM arm32v7/node:14.17.4

RUN apt update
#RUN apt -y upgrade
RUN apt install -y nano

#Installieren von NPM Abhängigkeiten
COPY package*.json ./

# Entwicklungsumgebung
WORKDIR /modules
COPY package.json .
RUN npm install
ENV NODE_PATH=/modules/node_modules

# Produktionsumgebung
#WORKDIR /modules
#COPY package.json .
#RUN npm ci --only=production
#ENV NODE_PATH=/modules/node_modules

# Node js wird im Benutzerverzeichnis gestartet
WORKDIR /home/node/app
COPY . .
WORKDIR /

# verkleinern des Images
RUN apt clean

EXPOSE 8081
CMD ["node", "server.js"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]