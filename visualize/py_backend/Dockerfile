FROM arm32v7/python:rc-buster

# Anlegen des Volume Ordners zum späteren Mounten
RUN mkdir /data

# Ausführung
ADD script.py /
CMD ["python3", "./script.py"]
