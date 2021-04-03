FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /strugal

COPY . .

# Install postgres client
RUN apk add --update --no-cache postgresql-client

# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev


RUN pip install -r requirements.txt

# Remove dependencies
RUN apk del .tmp-build-deps


