from flask import request, Flask, redirect, url_for
app=Flask(__name__)
@app.route('/')
def play():
    print('hhh')
    print(request.full_path)
    return redirect(url_for('login',next=request.full_path))

@app.route('/login')
def login():
    print('next;'+request.args.get('next'))
    return redirect(request.args.get('next'))
if __name__ == '__main__':
    app.run()