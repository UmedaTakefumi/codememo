# Dockerfile / 2020.12.19_loop_add_float
## usage:
##   docker build -t  ss-2020.11.28_wsgi-samples .
##   docker run   -it ss-2020.11.28_wsgi-samples /bin/bash
FROM centos:7

RUN yum -y update
RUN yum -y groupinstall "Development Tools"

RUN groupadd -g 10000 developer
RUN adduser -g 10000 -d /home/developer developer
USER developer

WORKDIR /home/developer/wsgi-sample
COPY index.py /home/developer/wsgi-sample
