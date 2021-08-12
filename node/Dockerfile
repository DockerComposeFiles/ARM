FROM arm32v7/node:14.17.4

RUN apt update
#RUN apt -y upgrade
RUN apt install -y nano

#Installieren von NPM Abhängigkeiten
COPY package*.json ./

# Entwicklungsumgebung
RUN npm install

# Produktionsumgebung
# RUN npm ci --only=production

RUN apt clean

# node js wird im Unterverzeichniss betrieben
WORKDIR /home/node/app
COPY . .
WORKDIR /

EXPOSE 8081
CMD ["node", "server.js"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]