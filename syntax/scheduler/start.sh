#!/bin/bash

# nohub style
nohup python3 ./send_data &
# Command line style
cli-app
# python style
/usr/bin/python ./python_app.py

/usr/local/app &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start app: $status"
  exit $status
else echo "app run"
fi

python3 /python_app.py &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start python_app: $status"
  exit $status
else echo "python_app run"
fi



