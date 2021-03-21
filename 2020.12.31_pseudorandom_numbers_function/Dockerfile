# Dockerfile / 2020.12.19_loop_add_float
## usage:
##   docker build -t ss-2020.12.19_loop_add_float .
##   docker run -it ss-2020.12.19_loop_add_float /bin/bash

FROM ubuntu:20.04

USER root
WORKDIR /root

## ref: https://qiita.com/yagince/items/deba267f789604643bab
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update
RUN apt-get -y install vim git

WORKDIR /root/source


