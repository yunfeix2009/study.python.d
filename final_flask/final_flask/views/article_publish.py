from flask import Blueprint, render_template,request, session, redirect, flash
from final_flask.sql_moudle import Sql_class, get_current_usr_zan_wz_list, get_all_display_wz_data, get_wz_html_data
from final_flask.forms import RegisterForm

article_publish = Blueprint('message_board', __name__, template_folder='templates', static_folder='static')


cls = Sql_class()
@article_publish.route('/', methods=['GET', 'POST'])
def index():
    return render_template('logins_2.html')


@article_publish.route('/homepage', methods=['post', 'get'])
def logins():
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get("password")
        print('homepage: username:' + str(username), 'password:' + str(password))
        get_now_user_pwd_sql = "select count(*) from usr where usr_name='" + username + "' and pwd='" + password + "'"
        print('homepage: get_now_user_pwd:' + get_now_user_pwd_sql)
        conn, cur = cls.get_conn()
        now_user_pwd = cls.query(cur, get_now_user_pwd_sql)
        print('homepage: n:' + str(now_user_pwd))
        cls.close(conn, cur)
        if int(now_user_pwd[0][0]) > 0:
            session['username'] = username
            session['password'] = password
            session.permanent = True
            session[username] = "success"
            return render_template('homepage.html', value=get_current_usr_zan_wz_list())
        else:
            return '<h1><span style="color:red"> 用户名或密码错误<span><h1>'
    else:
        return render_template('homepage.html', value=get_current_usr_zan_wz_list())


@article_publish.route('/wz_list')
def wz_list():
    return render_template('wz_list.html', value=get_all_display_wz_data())


@article_publish.route('/wz')
def wz():
    id = request.args.get('id')
    print(id)
    wz, zan = get_wz_html_data(id)
    print('wz')
    print(wz)
    print('***')
    print('zan')
    print(zan)
    print('***')
    author = wz[0][0]
    title = wz[0][1]
    content = wz[0][2]
    ls = []
    for i in zan:
        ls.append(i[0])
    likes = len(ls)
    usr = session['username']
    print('author')
    print(author)
    print('title')
    print(title)
    print('content')
    print(content)
    print('ls')
    print(ls)
    print('likes')
    print(likes)
    print('current_usr')
    print(usr)
    return render_template('wz.html', author=author, title=title, content=content, zaner=ls, likes=likes, usr=usr, id=id)


@article_publish.route('/author')
def author():
    return render_template('wz.html', value=get_all_display_wz_data())


@article_publish.route('/publish')
def publish():
    return render_template('publish_2.html')


@article_publish.route('/publish_content', methods=['post'])
def publish_content():
    username = session.get('username')
    title = request.form.get('title')
    arc_contents = request.form.get('arc_contents')
    conn, cur = cls.get_conn()
    publish_sql = "insert into wz_all(title,usr_name,content) values('" + title + "','" + username + "','" + arc_contents + "')"
    print('publish_content: publish_sql:' + publish_sql)
    cls.normal_ex(conn, cur, publish_sql)
    cls.close(conn, cur)
    return render_template('publish_content.html')


@article_publish.route('/join', methods=['GET', 'POST'])
def root():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.us.data
        pswd = form.ps.data
        pswd2 = form.ps2.data
        print(name, pswd, pswd2)
        return '注册成功'
    else:
        if request.method == 'POST':
            flash(u'信息有误，请重新输入！')
        print(form.validate_on_submit())
    return render_template('register_2.html', form=form)


@article_publish.route('/save_usr', methods=['post', 'get'])
def save_usr():
    username = request.form.get("us")
    password1 = request.form.get("ps")
    password2 = request.form.get("ps2")
    alias = request.form.get("alias")
    print('save_usr: usr_information:' + username)
    print('save_usr: usr_information:' + password1)
    print('save_usr: usr_information:' + password2)
    print('save_usr: usr_information:' + alias)
    if password1 == password2:
        conn, cur = cls.get_conn()
        save_usr_sql = "insert into usr values('" + username + "','" + password1 + "','" + alias + "')"
        print(save_usr_sql)
        cls.normal_ex(conn, cur, save_usr_sql)
        cls.close(conn, cur)
    return redirect("/")


@article_publish.route('/dian_zan')
def dian_zan():
    username = session['username']
    wz_id = request.args.get('wz_id')
    dian_zan_sql = "insert into zan values('" + username + "','" + wz_id + "')"
    conn, cur = cls.get_conn()
    cls.normal_ex(conn, cur, dian_zan_sql)
    cls.close(conn, cur)
    return render_template('homepage.html', value=get_current_usr_zan_wz_list())


@article_publish.route('/qu_xiao', methods=['post', 'get'])
def qu_xiao():
    username = session['username']
    wz_id = request.args.get('wz_id')
    dian_zan_sql = "delete from zan where wz_id='" + wz_id + "' and usr_id='" + username + "'"
    conn, cur = cls.get_conn()
    cls.normal_ex(conn, cur, dian_zan_sql)
    cls.close(conn, cur)
    return render_template('homepage.html', value=get_current_usr_zan_wz_list())


@article_publish.after_request
def after_request(response):
    print('Access to : ' + request.full_path)
    return response


@article_publish.before_request
def before_request():
    username = session.get('username')
    if request.path != "/login":
        if request.path == "/":
            pass
        elif request.path == "/homepage":
            pass
        elif request.path == "/join":
            pass
        elif request.path == "/save_usr":
            pass
        elif username == None or session.get(username) != 'success':
            return redirect("/")
