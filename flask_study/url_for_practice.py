from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route('/')
def index():
    login_url = url_for('login')
    print(login_url)
    return redirect(login_url)
@app.route('/login')
def login():
    return '这是登陆页面'
if __name__== '__main__':
    app.run(debug=True)