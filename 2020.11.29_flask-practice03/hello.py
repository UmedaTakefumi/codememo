from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    name = "Hello, World"
    return name


@app.route('/good')
def good():
    name = "Good"
    return name

@app.route("/<name>")
def hello_name(name):
  return "Hello, {}".format(name)


if __name__ == "__main__":
    app.run(debug=True)

# ref:
#   https://qiita.com/tomboyboy/items/122dfdb41188176e45b5
#   https://qiita.com/nagataaaas/items/d249c3905d41137cd510
