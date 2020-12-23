# uWSGI sample script 

## 

```
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
```

## uWSGIでの起動

```
uwsgi --workers 2 --http :4649 --wsgi-file /home/developer/wsgi-sample/index.py
```

## usage

```
docker run -it -p 4649:4649 ss-2020.11.28_wsgi-samples
```

## 参考にした情報

* https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
