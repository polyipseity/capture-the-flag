#!/bin/bash
docker rm -f ninja-club
docker rmi -f ninja-club
docker build -t ninja-club .
docker run -d --name=ninja-club --rm -p 8000:8000 -it ninja-club
