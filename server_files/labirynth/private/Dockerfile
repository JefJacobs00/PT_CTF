FROM python:3.11-slim

RUN apt-get update -y \
    && apt-get install --no-install-recommends -y socat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*



RUN adduser --disabled-password --gecos '' challenge
USER challenge

ENV PATH = "/home/challenge/.local/bin:${PATH}"

WORKDIR /app

COPY server.py /app/
copy serve.sh /app/


EXPOSE 1337

CMD chmod +x serve.sh
CMD /app/serve.sh
