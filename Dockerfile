FROM python:alpine

RUN mkdir -p /usr/src/newmamka
WORKDIR /usr/src/newmamka

CMD ["python3", "www/startserver.py"]