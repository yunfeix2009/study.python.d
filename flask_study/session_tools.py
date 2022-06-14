from flask import request,Flask,current_app,session,g
from datetime import timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 配置7天有效

#测试请求上下文request
@app.route('/request_context')
def request_context():
    user_agent = request.headers.get("User-Agent")
    return f"<h1>Hello World!</h1>\nHello World!{user_agent}"

#测试应用上下文current_app
@app.route("/currentapp_context")
def currentapp_context():
    return "hello %s" % current_app.name

# 设置session
@app.route('/set_session')
def set_session():
    session['username'] = 'steven'  # 设置“字典”键值对
    session['password'] = '123456'
    session.permanent = True  # 设置session的有效时间，长期有效，一个月的时间有效，
    return 'login success'

# 获取session
@app.route('/get_session')
def get_session():
    # 第一种session获取如果不存在会报错
    # session['username']
    # 推荐使用session.get('username')
    # session.get('username')
    return session.get('password')

# 删除session
@app.route('/delete_session/')
def delete_session():
    print(session.get('username'), session.pop('username', None))
    # 或者 session['username'] = False
    print(session.get('username'))
    return "delete session is success"


#清除session中所有数据
@app.route('/clear_session')
def clear_session():
    print(session.get('username'))
    # 清除session中所有数据
    session.clear()
    print(session.get('username'))
    return 'clear session is success'

#定义了一个方法，用g来获取一个name的值
def test_g():
    return g.get('name',"no name")


#测试应用上下文g
@app.route('/testG')
def test():
    g.name = '张三'
    test_g()
    return test_g()

#定义了一个提交的form
@app.route('/testRequest')
def test1():
    return '<form action="/getUser" method="get">  ' \
           '<input type="text" name="username" value="">  ' \
           '<input type="submit" value="提交">  ' \
           '</form>'

#测试请求上下文request
@app.route('/getUser',methods=['GET'])
def getUser():
    username=request.values.get('username')
    return "my name is "+username

if __name__ == '__main__':
    app.run(debug=True)