# Apache Standard

## Apache Ordnerstruktur
/var/www/conf/httpd.conf

/usr/local/apache/conf/httpd.conf

/etc/httpd/conf/httpd.conf

#### Die Webseite wird durch ein volume eingebunden. Diese muss mit diesem Befehl erzeugt werden:
sudo docker create -v /data/apache --name data-apache httpdv7:latest
#### Um das Netzwerk lokal verfügbar zu machen ist dieser Befehl notwendig:
sudo docker network create -d bridge --subnet 172.27.0.0/16 --gateway 172.27.0.1 elastic2ls-net2

