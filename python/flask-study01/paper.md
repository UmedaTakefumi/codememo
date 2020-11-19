sudo yum -y update
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
echo 'eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)' >> /home/vagrant/.bash_profile
eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
brew install pyenv
pyenv versions

sudo yum -y groupinstall 'Development tools' 

pyenv versions
pyenv install -l | grep -E "\s3." | sort -nr | head -5
pyenv install -l | grep -E "\s3.[0-9.]+$" | sort -nr | head -10 | xargs -I{} pyenv install {}
pyenv install -l | grep -E "\s3.[0-9.]+$" | sort -nr | head -5 | xargs -I{} pyenv install {}

yum localinstall http://dev.mysql.com/get/mysql57-community-release-el7-8.noarch.rpm
sudo yum localinstall http://dev.mysql.com/get/mysql57-community-release-el7-8.noarch.rpm
sudo yum install -y mysql-community-server

sudo yum -y install vim-enhanced.x86_64

sudo vim /etc/yum.repos.d/nginx.repo
yum -y install nginx
sudo yum -y install nginx
systemctl start nginx
sudo systemctl start nginx
sudo systemctl enable nginx
clear
systemctl list-unit-files --type=service

sudo systemctl start mysqld.service

pyenv versions
pyenv local 3.8.6
pyenv versions
pyenv versions
exec "$SHELL"
echo $PYENV_ROOT
pyenv 
ls
cd
cat .bash_profile 
clear
exec "$SHELL"
ls
pyenv
python
vim .pyenv/
ls
vim .bash_profile 
source .bash_profile 
ls

sudo systemctl start firewall 
sudo systemctl start firewalld
sudo systemctl enable firewalld
sudo firewall-cmd --add-service=http --permanent 

firewall-cmd --reload
sudo firewall-cmd --reload
sudo firewall-cmd --list-all-zones
sudo firewall-cmd --list-all-zones | less

cd codememo/
cd python/
cd Flask/
cd 01.helloworld/
cd codememo/
mkdir flask-study01
cd flask-study01/

pip3.8 install pipenv 
pyenv versions
pipenv install --python 3.8.6 
pipenv install --python 3.8.6 
python 
pip install pipenv 
pipenv install --python 3.8.6
pipenv shell
pipenv install uwsgi
sudo yum -y install libffi-devel
pipenv install uwsgi
sudo yum search libffi 
sudo yum -y install libffi-devel.x86_64 libffi.x86_64
sudo yum search python 
pipenv install uwsgi
pipenv install setuptools tokenize
pipenv install setuptools
pipenv install uwsgi
pipenv install tokenize
pipenv shell
pyenv versions 
pyenv uninstall 3.8.6
pyenv install 3.8.6
pipenv shell
pip3.8 pipenv 
pip3.8 install pipenv 
pip3.8 list
pyenv versions
pip install pipenv 
pip install --upgrade pip
pyenv versions
pipenv --python 3.8.6
pipenv install flask 
pipenv install uwsgi 
sudo yum -y search pcre
sudo yum -y install pcre-devel
sudo yum -y install pcre2-devel
pipenv install uwsgi 
pyenv versions
pyenv uninstall 3.8.6
pyenv install 3.8.6
LANG=C pyenv install 3.8.6
pyenv versions
pip install --upgrade pip
pip install pipenv
history | grep pip
pipenv install --python 3.86
pipenv install --python 3.8.6
pip list
pipenv shell
pipenv install flask
pipenv install uwsgi
rpm -qa | grep pcre
pyenv rehash 
pipenv install uwsgi
pip install uwsgi 
rpm -qa | grep pcre
sudo yum remove pcre-devel
sudo yum remove pcre2-devel
sudo yum install pcre2-devel
cd codememo/
cd python/
cd flask-study01/
pipenv install uwsgi
pipenv install SQLAlchemy Flask-SQLAlchemy Blueprint
