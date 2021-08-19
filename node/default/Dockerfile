FROM arm32v7/node AS base

RUN apt update
#RUN apt -y upgrade
RUN apt install -y nano && apt install tree
# verkleinern des Images
RUN apt clean

FROM base
# Installieren von NPM Abhängigkeiten
WORKDIR /modules
COPY package.json .
RUN if [ "$NODE_ENV" = "development" ]; \
        # Entwicklungsumgebung
	then npm install;  \
        # Produktionsumgebung
	else npm install --only=production; \
	fi
# Node Modulpfad
ENV NODE_PATH=/modules/node_modules

# Node js wird im Benutzerverzeichnis gestartet
WORKDIR /home/node/app
COPY . .

EXPOSE 80
CMD ["node", "server.js"]