#!/bin/sh
nohub /usr/local/apache2/bin/apachectl start &
nohup python3 ./send_data &
echo lastLine