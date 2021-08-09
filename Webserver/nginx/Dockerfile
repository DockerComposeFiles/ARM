FROM arm32v7/nginx

#RUN apt clean
RUN apt update
#RUN apt -y upgrade
RUN apt install -y nano

COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /
