from flask import Flask,render_template
import random
app = Flask(__name__,template_folder='211120')

@app.route("/")
def mainpage():
    return render_template('mainpage.html')
@app.route("/test1")
#定义第一页视图
def test1():
    goods = {'name':'包包', 'price':500,'number':'4','color':'red'},\
            {'name':'口红', 'price':300,'number':'4','color':'blue'}, \
            {'name':'冰淇淋', 'price':20,'number':'4','color':'yellow'}
    return render_template('test1.html', goods=goods)

@app.route("/test2")
#定义第一页视图
def test2():
    rad = random.randint(1, 4)
    goods = {'name':'包包', 'price':500,'number':'4','color':'red'},\
            {'name':'口红', 'price':300,'number':'4','color':'blue'}, \
            {'name':'转笔', 'price':230,'number':'10','color':'black'}, \
            {'name':'冰淇淋', 'price':20,'number':'4','color':'yellow'}
    #产生1~4范围内的随机整数
    return render_template('test2.html',number=rad,goods=goods)
@app.route('/test3')
def hello_num():
    list1 = []
    for i in range(10):
        list1.append(i)
    return render_template('test3.html', list1=list1)
@app.route('/base')
def base():
    content = 'helloWorld'
    return render_template('base.html',content=content)
@app.route('/test4')
def base_one():
    return render_template('one.html')
@app.route('/test2_1')
def test2_1():
    rad = random.randint(1, 4)
    goods = {'name':'包包', 'price':500,'number':'4','color':'red'},\
            {'name':'口红', 'price':300,'number':'4','color':'blue'}, \
            {'name':'转笔', 'price':230,'number':'10','color':'black'}, \
            {'name':'冰淇淋', 'price':20,'number':'4','color':'yellow'}
    return render_template('test2_1.html',number=rad,goods=goods)

@app.route("/base_01")
def base_01():
    return render_template('base_01.html')
if __name__ == '__main__':
    app.run()