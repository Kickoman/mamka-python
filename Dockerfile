FROM python:alpine

RUN mkdir -p /usr/src/newmamka
RUN pip3 install markdown
WORKDIR /usr/src/newmamka

CMD ["python3", "startserver.py"]
