from flask import Flask, request, g

app = Flask(__name__)


def test_g():
    return g.get('name', "no name")


@app.route('/testG')
def test():
    g.name = '张三'
    return test_g()


@app.route('/testRequest')
def test1():
    return '<form action="/getUser" method="get">  ' \
           '<input type="text" name="age" value="">  ' \
           '<input type="submit" value="提交">  ' \
           '</form>'


@app.route('/getUser', methods=['GET'])
def getUser():
    age = request.values.get('age', 10)
    return "my name is " + str(age)


# @app.route('/testRequest/testG/getUser/abc')
# def printout():
#    return 'hello'

if __name__ == '__main__':
    app.run()