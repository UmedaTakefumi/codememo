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


if __name__ == "__main__":
    app.run(debug=True, port=2000, host='0.0.0.0')

# ref:
# https://qiita.com/tomboyboy/items/122dfdb41188176e45b5
