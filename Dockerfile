FROM python:3.7-alpine

ENV PYTHONBUFFERED 1

ENV DJANGO_SECRET_KEY '_j$nc$l&xg)@iske_7ma+u4tfut!d9lp!*$qem*zc-)0%yw%#='
COPY ./requirements.txt /requirements.txt

RUN apk --update add \
    build-base \
    jpeg-dev \
    zlib-dev\
    libjpeg

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app


RUN adduser -D user
USER user
