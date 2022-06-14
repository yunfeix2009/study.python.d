# from flask import Flask,request,g
# app = Flask(__name__)
# def test_g():
#     return g.get('name',"no name")
# @app.route('/testG')
# def test():
#     g.name = '张三'
#     return test_g()
# @app.route('/testRequest')
# def test1():
#     return '<form action="/getUser" method="get">  ' \
#        '<input type="text" name="username" value="">  ' \
#        '<input type="submit" value="提交">  ' \
#        '</form>'
# @app.route('/getUser',methods=['GET'])
# def getUser():
#     username=request.values.get('username')
#     return "my name is "+username
# if __name__ == '__main__':
#     app.run()


class Student(object):
    name1 = "Tony"
    def __init__(self,name):
        self.self=name
    def eat(self,something):
        print("eat the ",something)
    @staticmethod
    def sleep():
        print("static method")
    @classmethod
    def goodstudy(cls):
        print("class method")
    @classmethod
    def setName(cls,name):
        print("class method")
        cls.name1 = name
if __name__ == '__main__':
    stud = Student("tom")
    stud.name1 = "lucy"
    print(stud.name1)
    stud.setName("abc")
    print(stud.name1)
    stud.goodstudy()
    Student.goodstudy()
    stud.sleep()
    Student.sleep()