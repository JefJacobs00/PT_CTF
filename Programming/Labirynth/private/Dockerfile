FROM python:3.8.12-slim

RUN apt-get update

RUN adduser --disabled-password --gecos '' challenge
RUN apt-get -y install socat
USER challenge

ENV PATH = "/home/challenge/.local/bin:${PATH}"

WORKDIR /app

COPY server.py /app/
copy serve.sh /app/

EXPOSE 1337

ENTRYPOINT ["/bin/sh", "/app/serve.sh"]
