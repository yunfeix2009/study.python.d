from flask import Flask, request, render_template, abort, jsonify, redirect

app = Flask(__name__)
error_list = []


@app.route('/')
def index():
    ### print(1/0)
    ### abort(404) #我们可以使用flask.abort手动抛出相应的错误
    return render_template("index.html", test2='I like coding')


@app.route('/user')
def user():
    user_agent = request.headers.get("User-Agent")
    return f"<h1>Hello World!</h1>\nHello World!{user_agent}"


@app.route('/commit')
def commit():
    return '<form action="/getUser" method="get">  ' \
           '<input type="text" name="username" value="">  ' \
           '<input type="submit" value="提交">  ' \
           '</form>'


@app.before_first_request
def before_first_request():
    print("call the before first request of function")


@app.before_request
def before_request():
    print("call the before request of function")


@app.after_request
def after_request(response):
    print("call the after request of function")
    ### print(response.get_json())
    # print(response.data)
    print(response.headers)
    ### return jsonify({"a": 1})
    return response


@app.teardown_request
def teardown_request(error):
    print("call the teardown request of function")
    print("the error is:", error)
    error_list.append(error)


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    print("call the teardown appcontext of function")
    if (exception is None):
        print("None")
    else:
        print("the exception is:", exception)
        ### db.close();
        ### file.close()


@app.route("/get_error")
def get_error():
    print(error_list)
    return str(error_list)


@app.template_filter("upper")
def upper_filter(str):
    print("call the upper filter of function")
    return str.upper() + " good good study"


@app.context_processor
def context_process():
    print("call the context process of function")
    abc = 'flask context manager'
    return dict(test='flask context manager', test1='I like study')


@app.errorhandler(500)
def server_is_exception(error):
    print("*" * 100)
    print(error)
    return 'the server is exception', 500


@app.errorhandler(404)
def page_not_found(error):
    print("*" * 50)
    print(error)
    return 'This page does not exist', 404


@app.route('/redirect')
def index_redirect():
    return redirect("http://baidu.com")


if __name__ == '__main__':
    app.run(debug=True)
