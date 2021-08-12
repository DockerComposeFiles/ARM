FROM arm32v7/node:14.17.4
RUN pwd
RUN apt update
#RUN apt -y upgrade
RUN apt install -y nano
RUN pwd && ls
# Installieren von NPM Abhängigkeiten
WORKDIR /modules
COPY package.json .
RUN if [ "$NODE_ENV" = "development" ]; \
        # Entwicklungsumgebung
	then npm install;  \
        # Produktionsumgebung
	else npm install --only=production; \
	fi
ENV NODE_PATH=/modules/node_modules
RUN pwd && ls
# Node js wird im Benutzerverzeichnis gestartet
WORKDIR /home/node/app
COPY . .
#WORKDIR /
RUN pwd && ls
# verkleinern des Images
#RUN apt clean

EXPOSE 8081
CMD ["node", "server.js"]