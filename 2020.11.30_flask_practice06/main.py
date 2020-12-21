from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main_page():
	return render_template("mainpage.html")

@app.route("/<name>", methods=["GET", "POST"])
def namapage(name):
	return render_template("name.html")

if __name__ == "__main__":
	app.run(debug=True)

## ref:
##	https://qiita.com/nagataaaas/items/4662237cfb7b92f0f839


