# Dockerfile / 2020.11.29_flask-practice01
## usage:
##   docker build -t  2020.11.29_flask-practice01 .
##   docker run   -it 2020.11.29_flask-practice01 /bin/bash
##   docker run -it -p 4649:4649 2020.11.29_flask-practice01
FROM centos:7

RUN yum -y update
RUN yum -y install vim-enhanced git which
RUN yum -y groupinstall "Development Tools"
RUN yum -y install zlib-devel bzip2-devel readline-devel \
		   sqlite-devel openssl-devel
RUN yum -y install libffi-devel libffi pcre2-devel

RUN groupadd -g 10000 developer
RUN adduser  -g 10000 -d /home/developer developer
USER developer
ENV HOME /home/developer

ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH
RUN curl https://bootstrap.pypa.io/get-pip.py | python 
RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
RUN echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc
RUN pyenv install 3.9.1
WORKDIR /home/developer
RUN pyenv local 3.9.1

WORKDIR /home/developer/flask-practice01
COPY hello.py /home/developer/flask-practice01
COPY Pipfile /home/developer/flask-practice01
COPY test_hello.py /home/developer/flask-practice01

RUN $HOME/.pyenv/shims/pip install pipenv
RUN $HOME/.pyenv/shims/pipenv install --python 3.9.1
RUN $HOME/.pyenv/shims/pipenv install flask uwsgi 

#COPY Pipfile.lock /home/developer/flask-practice01
CMD ["/home/developer/.pyenv/shims/pipenv", "run", "start"]

EXPOSE 4649 
