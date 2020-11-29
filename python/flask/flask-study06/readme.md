# 勉強


## モジュールをインストールする

```
pipenv update
```

## pipenv仮想環境にログインする

```
pipenv shell
```

## uwsgiでflask-appを起動する

Pipfileを編集する

```
start = "uwsgi --http :2000 --wsgi-file hello.py --callable app"
```

## pipenv仮想環境でアプリを起動する

```
pipenv run start
```



