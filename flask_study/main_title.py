from flask import render_template
from flask import redirect
from flask import request
from flask import Flask
import pymysql

app = Flask(__name__)


def connection_sql(data):
    db = pymysql.connect(host="localhost", user="root", password="password", database="database")
    db_curs = db.cursor()
    insert_sql = """INSERT INTI form_name(field_1, field_2, field_3) VALUES (value_1, value_2, value_3);"""
    try:
        db_curs.execute(insert_sql)
        db.commit()
        print("ok")
    except:
        db.rollback()
        print("insert error")
    db.close()

def find_all_user():
    mydb = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='wz',
        charset='utf8'
    )

    cur = mydb.cursor()
    cur.execute('SELECT * FROM usr')
    result = cur.fetchall()
    ret = {}
    for r in result:
        ret[r[0]]=r[1]
    return ret


app = Flask(__name__,template_folder='211120')
creater = find_all_user()

def find_all_data():
    all_contents_list=[]
    with open('D:\\dev\projs\\flask_study\\wz_publish_list_main', 'r',encoding='UTF-8') as f:
        for line in f:
            all_contents_list.append(line.split('/'))
    return all_contents_list


@app.route('/')
def index():
    return render_template('logins.html')

@app.route('/get_login')
def logins():
    username = request.args.get('username')
    password = request.args.get("password")
    print(username,password)
    if username in creater.keys():
        if password==creater[username]:
            return redirect('/menu')
        else:
            return '<h1><span style="color:red"> 用户名或密码错误<span><h1>'
    else:
        return '<h1><span style="color:blue"> 用户名或密码错误<span><h1>'

@app.route('/post_logins',methods=['post'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username,password)
    if username in creater.keys():
        if password==creater[username]:
            return redirect('/menu')
        else:
            return '<h1><span style="color:red"> 用户名或密码错误<span><h1>'
    else:
        return '<h1><span style="color:blue"> 用户名或密码错误<span><h1>'

@app.route('/display_all')
def display_all():
    return render_template('display_list.html',value=find_all_data())

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/search')
def main():
    """首页"""
    return render_template('search.html')

@app.route('/display')
def display():
    keyword_list=[]
    ls = find_all_data()
    key_word = request.args.get("key_word")
    for i in ls:
        if key_word in i[1]:
            keyword_list.append(i)
    return render_template('display_list.html',value=keyword_list)

@app.route('/publish')
def publish():
    return render_template('publish.html')

@app.route('/publish_content',methods=['post'])
def publish_content():
    """首页"""
    creater = request.form.get('creater')
    title = request.form.get('title')
    arc_contents = request.form.get('arc_contents')
    str = creater+"/"+title+"/"+arc_contents+'\n'
    with open('D:\\dev\projs\\flask_study\\wz_publish_list_main','a',encoding='UTF-8') as f:
        f.write(str)
    return render_template('display_list.html',value=find_all_data())

if __name__ == '__main__':
    app.run(debug=True)