FROM python:3.8-slim

WORKDIR /srv

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .
