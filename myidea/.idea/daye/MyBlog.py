from flask import Flask, request

stu_information = {"admin": "1234561"}
first_line = """<a href="/">Home</a>
<a href="/blogs">Blogs</a>
<a href="/about">About me</a>"""
app = Flask(__name__)


@app.route("/")
def index():
    return first_line + """
<h1>Hello.this is Steven's site!</h1>
<h3>You are not logged in, please<a href="/login">CLICK HERE</a>to log in.</h3>
"""


@app.route('/login')
def login():
    return first_line + """
<form action="/info" method="post">
    用户名: <input type="text", name="username"/>
    <br/>
    密&nbsp;&nbsp;&nbsp;码: <input style="margin-left:2px" type="password", name="passworld"/>
    <button>登陆</button>
</form>
"""


@app.route('/blogs')
def blogs():
    return first_line + """
<h1>This is my blogs.</h1>
"""


@app.route("/about")
def about():
    return first_line + """
<h1>l am a coding teacher. Call me: 010-101010101.</h1>
"""


@app.route("/info", methods=["post"])
def get_info():
    user = request.form.get("username")
    psd = request.form.get("passworld")
    if stu_information.get(user):
        if psd == stu_information[user]:
            return "<h1>恭喜您，登录成功</h1><a href='/blogs'>点击可跳转到博客页</a>"
        else:
            return "<h1>登录失败，密码不对!</h1><a href='/'>请跳转到主页,重新登陆</a>"
    else:
        return "<h1>登录失败，用户名不存在!</h1><a href='/'>请跳转到主页,重新登陆</a>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
