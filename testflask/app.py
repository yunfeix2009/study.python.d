from flask import render_template, request, flash, session, redirect, Response, make_response
import os
from datetime import timedelta
import random
from tools.utils import *

basepath = ''

app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 配置7天有效
# resp = make_response('successfully_set_cookie')
resp = Response('successfully_set_cookie')


guest_available_list = ['/', '/login', '/register', '/guess_num/', '/guess_num/rule', '/guess_num/view_room_num', '/mail_sender/', '/mail_sender/send','/article_publish/', '/my_account', '/confirm_email', '/active_statu']


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        name = resp.headers[2][1].split(';')[0].split('=')[1]
        return render_template('./home_page_templates/home_page_1.html', basepath=basepath, alias=name)
    except:
        print('in except')

    if session.get(request.cookies.get('username')) == 0:
        return render_template('./home_page_templates/admin.html', basepath=basepath)

    elif session.get(request.cookies.get('username')) == 1:
        return render_template('./home_page_templates/home_page_1.html', basepath=basepath,
                               username=session['username'])
    elif (request.method == 'POST'):

        username = request.form.get('username')
        password = request.form.get('password')
        user_password = get_user_password()
        print(request.cookies.get('username'))
        if user_password[username] == password:
            user_role = get_user_role()
            alias = get_alias(username)
            resp.set_cookie('username', username)
            if user_role[username] == 0:
                session.permanent = True
                session[username] = 0
                return render_template('./home_page_templates/admin.html', basepath=basepath)
            else:

                session.permanent = True
                session[username] = 1
                return render_template('./home_page_templates/home_page_1.html', basepath=basepath, alias=alias)
        else:
            flash('用户名或密码错误')
            return render_template('./home_page_templates/home_page_login.html', basepath=basepath)

    else:
        return render_template('./home_page_templates/home_page_login.html', basepath=basepath)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        user_password = get_user_password()
        print(user_password)
        if user_password[username] == password:
            user_role = get_user_role()
            resp.set_cookie('username', username)
            if user_role == 0:
                flash('您好，尊敬的管理员')

                return render_template('./home_page_templates/admin.html', basepath=basepath)
            else:
                flash('登录成功')
                return render_template('./home_page_templates/home_page_login.html', basepath=basepath)
        else:
            flash('用户名或密码错误')
            return render_template('./home_page_templates/login.html', basepath=basepath)
    else:
        return render_template('./home_page_templates/login.html', basepath=basepath)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if (request.method == 'POST'):
        users = get_users()
        print(users)
        name = request.form.get('username')
        alias = request.form.get('alias')
        email = request.form.get('email')
        password = request.form.get('pass')
        repassword = request.form.get('repass')
        if password != repassword:
            flash('密码不一致')
        elif name in users:
            flash('用户名已存在， 请更换')
        else:
            usercol = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ', 16))
            print('usercol:', usercol)
            add_user(name, password, email, alias, usercol)
            id = get_id(name)
            return render_template('./home_page_templates/confirm_email.html', basepath=basepath, email_address=email,
                                   alias=alias, usercol=usercol, id=id)
    else:
        return render_template('./home_page_templates/register.html', basepath=basepath)


@app.route('/confirm_email')
def confirm_email():
    email_address = request.args.get('email_address')
    usercol = request.args.get('usercol')
    alias = request.args.get('alias')
    id = request.args.get('id')
    print(id)
    send_mail(email_address, alias, id, usercol)
    return '已发送'


@app.route('/active_statu')
def active_statu():
    id = request.args.get('id')
    usercol = request.args.get('usercol')
    id_usercol = get_id_usercol()
    print('id_usercol:', id_usercol)
    print(id)
    print(usercol)
    print(id_usercol[int(id)])
    if id_usercol.get(int(id))==usercol:
        update_active_statu(1, id)
        return redirect('/')


# @app.after_request
# def after_request(response):
#     ip = request.remote_addr
#     # logger.critical('ip: ' + ip + 'entering after_request route in article_publish')
#     print('Access to : ' + request.full_path)
#     return response
#
#
@app.before_request
def before_request():
    try :
        resp.headers[2][1].split(';')[0].split('=')[1]
    except:
        if request.path in guest_available_list or '/static' in request.path:
            pass
        else:
            return render_template('./home_page_templates/no_permission.html', current_url=request.path)
#     username = session.get('username')
#     if request.path != "/login":
#         if request.path == "/":
#             pass
#         elif request.path == "/homepage":
#             pass
#         elif request.path == "/join":
#             pass
#         elif request.path == "/save_usr":
#             pass
#         elif username == None or session.get(username) != 'success':
#             return redirect("/")

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0')
