#!/bin/sh

# NOCH Zwischengespeichert

# Apache Frontend
#/usr/local/apache2/bin/apachectl &
#status=$?
#if [ $status -ne 0 ]; then
#  echo "Failed to start Apache_Frontend: $status"
#  exit $status
#else echo "Apache arbeitet"
#fi
#
#echo "start Apache fin"
#sleep 10
#echo "10 sec vergangen"

# Python Backend
python3 /send_data.py &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start Backend: $status"
  exit $status
else echo "Python-Backend run"
fi

echo "start backend fin"
sleep 10
echo "2 x 10 sec vergangen"

# nohub Schreibweise
#nohup python3 ./send_data &
echo "start.sh_finished"
