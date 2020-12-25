# Dockerfile / 2020.12.19_loop_add_float
## usage:
##   docker build -t  2020.11.28_wsgi-samples .
##   docker run   -it 2020.11.28_wsgi-samples /bin/bash
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

WORKDIR /home/developer/wsgi-sample
RUN pyenv local 3.9.1
RUN $HOME/.pyenv/shims/pip install uwsgi
RUN $HOME/.pyenv/shims/pip install pytest

COPY index.py /home/developer/wsgi-sample
COPY test_index.py /home/developer/wsgi-sample

CMD ["/home/developer/.pyenv/shims/uwsgi", "--workers", "2", "--http", ":4649", "--wsgi-file", "/home/developer/wsgi-sample/index.py"]

EXPOSE 4649 
