FROM cimg/python:3.8.10 AS build

RUN sudo mkdir -p /app
WORKDIR /app

COPY . .

RUN cd app && poetry install
