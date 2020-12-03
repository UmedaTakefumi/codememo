
```
sudo vi /etc/yum.repos.d/mongodb-org-4.0.repo
```

```
[mongodb-org-4.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc
```

```
sudo yum install -y mongodb-org
```

* [CentOS7 に MongoDB を導入する方法 - Qiita](https://qiita.com/tomy0610/items/f540150ac8acaa47ff66)
* [Install MongoDB Community Edition on Red Hat or CentOS — MongoDB Manual](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/)
