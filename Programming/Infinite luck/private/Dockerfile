FROM python:3.8.12-slim

RUN apt-get update

RUN adduser --disabled-password --gecos '' challenge
USER challenge

ENV PATH = "/home/challenge/.local/bin:${PATH}"

WORKDIR /app

COPY server.py /app/
EXPOSE 65432

ENTRYPOINT ["python3", "-u", "server.py"]
