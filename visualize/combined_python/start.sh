@start /usr/local/apache2/bin/apachectl &
nohup python3 ./send_data &
echo lastLine