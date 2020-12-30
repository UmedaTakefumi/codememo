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




## 参考にした情報

* https://qiita.com/tomboyboy/items/122dfdb41188176e45b5
* https://pipenv-ja.readthedocs.io/ja/translate-ja/advanced.html
