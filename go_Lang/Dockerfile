FROM arm32v7/golang AS go

# Updaten des Images
RUN apt update --no-cache
#RUN apt -y upgrade
RUN apt install -y nano && apt install tree
#RUN apt clean

FROM go

WORKDIR /go/src/app
COPY . .

RUN go get -d -v ./...
RUN go install -v ./...

CMD ["app"]