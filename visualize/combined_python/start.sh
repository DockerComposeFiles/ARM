#!/bin/sh

# Alternativ kann auch supervisor genutzt werden

# Python Backend
python3 /send_data.py -D
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start Backend: $status"
  exit $status
fi

sleep 10

# Apache Frontend
/usr/local/apache2/bin/apachectl -D
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start Apache_Frontend: $status"
  exit $status
fi

sleep 60

# nohub Schreibweise
#nohup python3 ./send_data &
echo start.sh_finished
