#!/bin/sh
socat \
  -T15 \
  TCP-LISTEN:1337,reuseaddr,fork \
  EXEC:"timeout 1200 python server.py"