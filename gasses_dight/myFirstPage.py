from flask_study.Flask import Flask
from flask_study.Flask import request
import json


app = Flask(__name__)


@app.route("/")
def main_page():
    user_agent = json.dumps(dict(request.headers), indent=2)
    return f"<h1>Hello World!</h1>\nHello World!{user_agent}"


@app.route("/login")
def login_page():
    psw = "123"

    def check_psw(psw):
        return False

    return "<h1>login!</h1>" if check_psw(psw) else "<h1>False!</h1>"


@app.route("/static/<filename>")
def get_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    return text


@app.route("/secret")
def secret_page():
    return "<h1>secret!!!!</h1>", 400


@app.route("/any")
def not_found_page():
    return "<h1>not found!!!!</h1>", 404


if __name__ == "__main__":
    app.run(debug=True)
