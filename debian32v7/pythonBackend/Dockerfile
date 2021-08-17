# FROM arm32v7/python:rc-buster
FROM python:rc-buster AS python_socket

# Updaten des Images
RUN apt update --no-cache
#RUN apt -y upgrade
RUN apt install -y nano && apt install tree
#RUN apt clean

# Bibliothek zum senden der Daten
RUN pip install websockets

FROM python_socket
ADD script.py /
CMD ["python3", "./script.py"]