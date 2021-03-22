from flask import Flask, render_template
import util.html, util.network

app = Flask(__name__)


@app.route("/hello")
@util.html.h1
@util.html.em
def hello():
    return "hello"


@app.route("/")
def home():
    return render_template("robb.html")


if __name__ == "__main__":
    ipaddress = util.network.get_ipaddress()
    print(ipaddress)
    app.run(debug=True, host=ipaddress)
