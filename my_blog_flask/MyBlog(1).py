import os
from flask_study.Flask import Flask, request, session


stu_information = {"admin": "1234561","steven":"34561"}
first_line = """<a href="/">Home</a>
<a href="/blogs">Blogs</a>
<a href="/about">About me</a>
<br/>
"""
login_text = """
<form action="/info" method="post">
    用户名: <input type="text", name="username"/>
    <br/>
    密&nbsp;&nbsp;&nbsp;码: <input style="margin-left:2px" type="password", name="passworld"/>
    <button>登陆</button>
</form>
"""

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def index():
    text = first_line + "<h1>Hello.this is Steven's site!</h1>"
    if session.get("user"):
        return text + f"Hi,{session.get('user')}"
    else:
        text += "<h3>You are not logged in, please"
        text += "<a href='/login'>CLICK HERE</a>to log in.</h3>"
    return text


@app.route('/login')
def login():
    if not session.get("user"):
        return first_line + login_text
    else:
        return first_line + "您已经登陆,是否要<a href='/cancel'>取消登录</a>"


@app.route("/cancel")
def logout():
    if session.get("user"):
        del session["user"]
        return first_line + "您的登陆已注销!"
    else:
        return first_line + "请您先回到首页登陆"


@app.route('/blogs')
def blogs():
    if session.get("user"):
        return first_line + "<h1>This is my blogs.</h1>"
    else:
        return first_line + "请您先回到首页登陆"


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
            session["user"] = user
            return "<h1>恭喜您，登录成功</h1><a href='/blogs'>点击可跳转到博客页</a>"
        else:
            return "<h1>登录失败，密码不对!</h1><a href='/'>请跳转到主页,重新登陆</a>"
    else:
        return "<h1>登录失败，用户名不存在!</h1><a href='/'>请跳转到主页,重新登陆</a>"


if __name__ == '__main__':
    app.run(debug=True)
