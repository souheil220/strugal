FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /strugal

COPY . .

RUN pip install -r requirements.txt



