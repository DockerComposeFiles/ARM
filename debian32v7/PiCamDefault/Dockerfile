FROM arm32v7/python:rc-buster
ADD script.py /
RUN apt clean
RUN apt update
RUN pip install picamera
CMD [ "python", "./script.py" ]