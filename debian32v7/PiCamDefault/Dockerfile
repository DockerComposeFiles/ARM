# FROM arm32v7/python:rc-buster
FROM arm32v7/python
ADD script.py /
RUN pip install picamera
CMD [ "python", "./script.py" ]