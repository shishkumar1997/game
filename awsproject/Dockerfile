FROM python:3.8

ENV PYTHONUNBUFFERED 1  

WORKDIR /home/admin2/Documents/game/game/awsproject/

COPY requirement.txt ./

RUN pip uninstall django

RUN pip install -r requirement.txt