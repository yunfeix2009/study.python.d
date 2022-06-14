from flask import Flask, request, redirect

app = Flask(__name__)
user_dict = {'username': 'root', 'pwd': '123'}


@app.route('/')
def hello():
    success = request.args.get("success")
    abc = request.args.get("abc")
    print(success)
    print(abc)
    if success == '1':
        return f"<h1>Hello World!</h1><br>登录成功"
    else:
        return f"<h1>Hello World!</h1><br><a href='/login'> 需要登录 </a>"


@app.route('/login')
def commit():
    return '<form action="/submit" method="get">  ' \
           'User Name: <input type="text" name="username" value="">  ' \
           '<br>' \
           'Password: <input type="password" name="pwd" value="">  ' \
           '<br>' \
           '<input type="submit" value="提交">  ' \
           '</form>'


@app.route('/submit')
def submit1():
    username = request.args.get("username")
    password = request.args.get("pwd")
    if username == user_dict['username'] and password == user_dict['pwd']:
        print('success')
        return redirect('/?success=1&abc=6')
    else:
        print('failed')
        return redirect("http://www.baidu.com")


if __name__ == '__main__':
    app.run(debug=True)
