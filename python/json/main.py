#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

url = 'https://www.craneto.co.jp/study_sample/simple_json_file.json'
res = requests.get(url)

#print(res.text)

# json_loads() でPythonオブジェクトに変換
#data = json.loads(res.read().decode('utf-8'))
data = json.loads(res.text.decode('utf-8'))
print(data['title'])
print(data['author'])
print(data['description'])
for item in data['pages']:
        print(item['title'], ':', item['url'])

"""
参考情報

Requests: 人間のためのHTTP — requests-docs-ja 1.0.4 documentation
http://requests-docs-ja.readthedocs.io/en/latest/

Python3 で JSON の読み書きをする方法（WebAPI にも対応） – サンプルコード付 | Crane & to.
https://www.craneto.co.jp/archives/1331/

19.2. json — JSON エンコーダおよびデコーダ — Python 3.6.1 ドキュメント
https://docs.python.jp/3/library/json.html

"""



