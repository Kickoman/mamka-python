FROM python:alpine

RUN mkdir -p /usr/src/newmamka
RUN pip3 install markdown
RUn pip3 install requests
WORKDIR /usr/src/newmamka

CMD ["python3", "startserver.py"]
