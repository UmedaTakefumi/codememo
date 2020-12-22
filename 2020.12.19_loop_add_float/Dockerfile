# Dockerfile / 

## docker build -t ss-2020.12.19_loop_add_float .
## docker run -it ss-2020.12.19_loop_add_float /bin/bash
FROM ubuntu:20.04

USER root
WORKDIR /root

## ref: https://qiita.com/yagince/items/deba267f789604643bab
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update
RUN apt-get -y install vim git

# Python 3.9.0 (default, Dec  6 2020, 18:02:34) 
RUN apt-get -y install python3 

# go version go1.13.8 linux/amd64
RUN apt-get -y install golang

# ruby 2.7.0p0 (2019-12-25 revision 647ee6f091) [x86_64-linux-gnu]
RUN apt-get -y install ruby2.7

WORKDIR /root/source

## go
COPY loop-int-go.go /root/source
COPY loop-float-go.go /root/source

## perl
COPY loop-float-perl.pl /root/source

## python
COPY loop-float-python.py /root/source

## ruby
COPY loop-float-ruby.rb /root/source

RUN chmod 777 /root/source/*.py
RUN chmod 777 /root/source/*.go
RUN chmod 777 /root/source/*.rb
RUN chmod 777 /root/source/*.pl

