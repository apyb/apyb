FROM python:3
ENV PYTHONUNBUFFERED 1
ENV DATABASE_URL "postgres://postgres:postgres@localhost/db"
VOLUME /src
WORKDIR /src
ADD requirements.txt /src/
RUN pip install -r requirements.txt
ADD . /src/
