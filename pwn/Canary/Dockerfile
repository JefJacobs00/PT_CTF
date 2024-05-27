FROM ubuntu AS builder
RUN uname -a
RUN dpkg --add-architecture i386

RUN apt-get update && apt-get install -y --no-install-recommends make gcc-multilib libc6-dev libssl-dev openssl libssl-dev:i386 libc6-dev:i386
RUN apt-get update && apt-get install -y libc6-dev socat libssl-dev libssl-dev:i386 libc6-dev:i386 && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
WORKDIR /app
COPY ./src/ /app

RUN make canary


RUN apt-get install -y socat
EXPOSE 9991
ENTRYPOINT ["sh", "-c", "socat TCP-LISTEN:9991,reuseaddr,fork EXEC:./canary"]

