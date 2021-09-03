# FROM arm32v7/python:rc-buster
FROM python:rc-buster AS python_def

# Updaten des Images
RUN apt update
RUN apt -y upgrade
RUN apt install -y nano && apt install tree

FROM python_def AS web_backend

# Bibliothek zum senden der Daten
RUN pip install websockets
# Anlegen des Volume Ordners zum späteren Mounten
RUN mkdir /data

FROM web_backend AS website

# Apache Dateieen und statische Webseite
COPY /htdocs/ /usr/local/apache2/htdocs/
COPY httpd.conf /usr/local/apache2/httpd.conf

# Port ist im compose Festgelegt
EXPOSE 433 80

RUN apt clean

# Ausführung
ADD send_data.py /
#CMD ["python3", "./send_data.py"]
#CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
