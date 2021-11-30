FROM python:3.7-slim-buster
ENV PYTHONUNBUFFERED 1
VOLUME /src
WORKDIR /src
ADD requirements.txt /src/
RUN pip install -r requirements.txt
ADD . /src/
