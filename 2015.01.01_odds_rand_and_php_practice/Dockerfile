# Dockerfile / 2020.11.29_flask-practice01
## usage:
##   docker build -t  2015.01.01_odds_rand_and_php_practice .
##   docker run   -it 2015.01.01_odds_rand_and_php_practice /bin/bash
##   docker run -it -p 4649:4649 2015.01.01_odds_rand_and_php_practice
FROM php:7.4.13

USER root
WORKDIR /root

## ref: https://qiita.com/yagince/items/deba267f789604643bab
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update
RUN apt-get -y install vim git

WORKDIR /root/source
COPY mt_rand.php /root/source

