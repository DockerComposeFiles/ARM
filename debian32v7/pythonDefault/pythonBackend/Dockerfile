# FROM arm32v7/python:rc-buster
FROM python:rc-buster AS python_def

# Updaten des Images
RUN apt update
#RUN apt -y upgrade
RUN apt install -y nano && apt install tree
RUN apt clean

FROM python_def
# Bibliothek zum senden der Daten
RUN pip install websockets
ADD script.py /
CMD ["python3", "./script.py"]