FROM python:3
ADD https://github.com/DockerComposeFiles/ARM/blob/main/alpine32v7/CamDef/script.py /
RUN pip install picamera
CMD [ "python", "./script.py" ]