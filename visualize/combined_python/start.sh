#!/bin/sh
# Alternativ kann auch supervisor genutzt werden,
# um beide Prozesse zu starten

# Apache Frontend
/usr/local/apache2/bin/apachectl &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start Apache_Frontend: $status"
  exit $status
else echo "Apache arbeitet"
fi

echo "start Apache fin"
sleep 10
echo "10 sec vergangen"


echo "start.sh_finished"
