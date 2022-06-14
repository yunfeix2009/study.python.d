from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def helloworld():
    return render_template('index.html')

@app.route('/user/<username>')
def shou_user_info(username):
    return render_template('user.html',name=username)

if __name__ == '__main__':
    app.run()