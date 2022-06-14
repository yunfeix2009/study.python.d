from session_tools import request, Flask, current_app, session
from datetime import timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


@app.route('/request_context')
def request_context():
    user_agent = request.headers.get("User-Agent")
    return f"<h1>Hello World!</h1>\nHello World!{user_agent}"


@app.route("/currentapp_context")
def currentapp_context():
    return "hello %s" % current_app.name


@app.route('/set_session')
def set_session():
    session['username'] = 'steven'
    session['password'] = '123456'
    return 'login success'


@app.route('/get_session')
def get_session():
    return session.get('username')


@app.route('/delete_session/')
def delete_session():
    print(session.get('username'), session.pop('username', None))
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
