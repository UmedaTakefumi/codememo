from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def odd_even():
	if request.method == "GET":
		return """
		下に整数を入力してください。奇数か偶数か判定します
		<form action="/" method="POST">
		<input name="num"></input>
		</form>"""
	else:
		try:
			return """
			{}は{}です！
		        <form action="/" method="POST">
        		<input name="num"></input>
        		</form>""".format(str(request.form["num"]), ["偶数", "奇数"][int(request.form["num"]) % 2])
		except:
			return """
				有効な数字ではありません！入力しなおしてください。
                    <form action="/" method="POST">
                    <input name="num"></input>
                    </form>
			"""

if __name__ == "__main__":
    app.run(debug=True)

# ref:
#   https://qiita.com/tomboyboy/items/122dfdb41188176e45b5
#   https://qiita.com/nagataaaas/items/d249c3905d41137cd510
#   https://qiita.com/nagataaaas/items/3116352da186df102d96

