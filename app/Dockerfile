FROM python:3.8.7-slim-buster

RUN mkdir -p /project/config
ARG dir=/project/
COPY app/requirements.txt $dir/requirements.txt
WORKDIR $dir

RUN apt update \
  && apt install -y gcc
RUN pip install -r requirements.txt

ENTRYPOINT [ "uwsgi", "--ini", "/project/uwsgi.ini" ]
