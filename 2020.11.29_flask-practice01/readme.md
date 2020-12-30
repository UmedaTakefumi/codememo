# Flask sample script

## sake

* Flaskを利用してwebサーバを立ち上げる
* Flaskのルーティング記述を学ぶ
* Pipenvの使い方を学ぶ(これが主目的)

## pipenv仮想環境を構築する

```
pip install pipenv
```

利用するpythonのバージョンを指定する

```
pipenv install --python 3.9.1
```

利用するモジュールをpipではなく、pipenvでインストールする。

```
pipenv install flask uwsgi 
```

Pipfileの記述

[Pipfile](Pipfile)

pipenv環境でFlask環境を起動する

```
pipenv run start
```

なにか作業をしたいとき

```
pipenv shell
```

pip freezeのようなことをしたいとき

```
pipenv lock --requirements > requiments.txt
```

## Flask

* デコレーターを利用し、ルーティングを作成

## usage

```
git clone https://github.com/UmedaTakefumi/stock_scripts.git
```

```
cd stock_scripts/2020.11.29_flask-practice02
docker build -t 2020.11.29_flask-practice02 .
docker run -it -p 4649:4649 2020.11.29_flask-practice02
```

```
./test_hello.py
```

## 参考にした情報

* https://qiita.com/tomboyboy/items/122dfdb41188176e45b5
* https://pipenv-ja.readthedocs.io/ja/translate-ja/advanced.html
