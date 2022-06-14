import json
dict = {'a': 'wo', 'b': 'zai', 'c': 'zhe', 'd': 'li'}
string = json.dumps(dict)
print(dict)
print(string)
print(type(dict))
print(type(string))

# import json
loads = json.loads(string)
print(loads)
print(type(loads))
print(loads['a'])


dict = {'a': 'wo', 'b': 'zai', 'c': 'zhe', 'd': 'li'}
json.dump(dict,open(r'test.json','w'))
jsObj = json.load(open(r'test.json'))
print(jsObj)
print(type(jsObj))

from flask_study.Flask import request, Flask,current_app,session
from datetime import timedelta
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config.setdefault('SECRET_KEY',os.urandom(24))
@app.route('/')
def main_page():
    return '<h1>hello  steven  today</h1>'
@app.route('/User-Agent')
def request_context():
    user_agent = request.headers.get("User-Agent")
    ### return "<p>Your browser is %s</p>" % user_agent
    return f"<h1>Hello World!</h1>\nHello World!{user_agent}"
@app.route("/currentapp_context")
def currentapp_context():
    return "hello %s" % current_app.name
@app.route('/set_session')
def set_session():
    session['username'] = 'steven'  ### 设置“字典”键值对
    session['password'] = '123456'
    session.permanent = True  ### 设置session的有效时间，长期有效，一个月的时间有效，
    return 'login success'

@app.route('/get_session')
def get_session():
    return session.get('password')



@app.route('/delete_session/')
def delete_session():
    print(session.get('username'), session.pop('username', None))
    ### 或者 session['username'] = False
    print(session.get('username'))
    return "delete session is success"
@app.route('/clear_session')
def clear_session():
    print(session.get('username'))
    session.clear()
    print(session.get('username'))
    return 'clear session is success'
if __name__ == '__main__':
    app.run(debug=True)

