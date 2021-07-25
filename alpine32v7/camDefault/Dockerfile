FROM python:3
ADD https://raw.githubusercontent.com/DockerComposeFiles/ARM/main/alpine32v7/camDefault/script.py /script.py
RUN pip install picamera
CMD [ "python", "./script.py" ]