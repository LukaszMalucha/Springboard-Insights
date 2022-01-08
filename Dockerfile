FROM python:3.10.1-buster
MAINTAINER Lukasz Admin

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app

COPY ./app/ /app
COPY ./scripts /scripts
RUN chmod +x /scripts/*
WORKDIR /app


RUN useradd user
USER user

EXPOSE 8000


CMD ["entrypoint.sh"]

