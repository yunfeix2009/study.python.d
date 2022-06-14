from session_tools import Flask, request

app = Flask(__name__)


@app.route("/")
def main_page():
    user_agent = request.headers.get("User-Agent")
    return f"<h1>Hello World!</h1>\nHello World!{user_agent}"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
