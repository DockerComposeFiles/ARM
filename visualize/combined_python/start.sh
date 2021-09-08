#!/bin/sh
# Alternativ kann auch supervisor genutzt werden,
# um beide Prozesse zu starten

# Apache Frontend
/usr/local/apache2/bin/apachectl &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start Apache_Frontend: $status"
  exit $status
else echo "Apache run"
fi

sleep 1
echo "start Apache finished"

# Python Backend
python3 /send_data.py
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start Backend: $status"
  exit $status
else echo "Python-Backend run"
fi

sleep 60

# nohub Schreibweise
#nohup python3 ./send_data &
echo "start.sh_finished"
