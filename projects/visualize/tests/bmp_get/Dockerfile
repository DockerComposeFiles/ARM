FROM python:rc-buster AS python_def

# Updaten des Images
RUN apt update
#RUN apt -y upgrade
RUN apt install -y nano && apt install tree
RUN apt clean

FROM python_def
# Anlegen des Volume Ordners zum späteren Mounten
RUN mkdir /data

# Ausführung
ADD script.py /
CMD ["python3", "./script.py"]
