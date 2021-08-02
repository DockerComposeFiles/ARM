# FROM arm32v7/python:rc-buster
FROM arm32v7/python
ADD script.py /
RUN apt update
RUN pip install picamera
CMD [ "python", "./script.py" ]