FROM arm32v7/python:rc-buster
ADD script.py /
RUN apt update
RUN pip install picamera
CMD [ "python", "./script.py" ]