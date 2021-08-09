FROM arm32v7/httpd

#RUN apt clean
RUN apt update
#RUN apt -y upgrade
RUN apt install -y nano

COPY /website/ /usr/local/apache2/htdocs/
COPY httpd.conf /usr/local/apache2/httpd.conf

#CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
EXPOSE 433 80
