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

ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH
RUN curl https://bootstrap.pypa.io/get-pip.py | python 
RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
RUN  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
RUN echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
RUN echo 'echo "a"' >> ~/.bash_profile




