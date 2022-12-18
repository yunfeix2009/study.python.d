from views import app
from tools.models import sql
import smtplib
from email.mime.text import MIMEText

def get_user_password():
    conn, cur = sql.get_conn()
    get_user_info_sql = 'select username, password from users'
    user_password_tuple = sql.query(cur, get_user_info_sql)
    sql.close(conn, cur)
    user_password = {}
    for i in user_password_tuple:
        user_password[i[0]] = i[1]
    print(user_password)
    return user_password


def get_id_usercol():
    conn, cur = sql.get_conn()
    get_id_usercol_sql = 'select id, usercol from users'
    id_usercol_tuple = sql.query(cur, get_id_usercol_sql)
    sql.close(conn, cur)
    user_password = {}
    for i in id_usercol_tuple:
        user_password[i[0]] = i[1]
    print(user_password)
    return user_password



def get_user_role():
    conn, cur = sql.get_conn()
    get_user_info_sql = 'select username, role from users'
    user_role_tuple = sql.query(cur, get_user_info_sql)
    sql.close(conn, cur)
    user_role = {}
    for i in user_role_tuple:
        user_role[i[0]] = i[1]
    print(user_role)
    return user_role


def get_users():
    conn, cur = sql.get_conn()
    get_user_info_sql = 'select username, password, role from users'
    users_tuple = sql.query(cur, get_user_info_sql)
    sql.close(conn, cur)
    users = []
    for i in users_tuple:
        users.append(i)
    print(users)
    return users


def get_id(username):
    conn, cur = sql.get_conn()
    get_id_sql = 'select id from users where username="'+username+'"'
    id_tuple = sql.query(cur, get_id_sql)
    id=id_tuple[0][0]
    return id

def get_alias(username):
    conn, cur = sql.get_conn()
    get_alias_sql = 'select alias from users where username="{0}"'.format(username)
    alias_tuple = sql.query(cur, get_alias_sql)
    alias=alias_tuple[0][0]
    return alias



def add_user(username, password, email_address, alias, usercol):
    conn, cur = sql.get_conn()
    add_user_sql = 'insert into users(alias, email_address, password, username, usercol) values("' + alias + '","' + email_address + '","' + password + '","' + username + '","' + usercol + '")'
    print(add_user_sql)
    sql.normal_ex(conn, cur, add_user_sql)
    sql.close(conn, cur)



def update_active_statu(set_active, id):
    conn, cur = sql.get_conn()
    update_active_statu_sql = 'update users set active_statu = "' + str(set_active) + '" where(id=' + str(id) + ')'
    sql.normal_ex(conn, cur, update_active_statu_sql)
    sql.close(conn, cur)



def send_mail(recipient, alias, id, usercol):
    me = "hello" + "<" + app.config['MAIL_USERNAME'] + ">"
    msg = MIMEText(app.config['MAIL_CONTENT'].format(alias, app.config['ACTIVE_LINK'].format(id, usercol)), _subtype='html', _charset='gb2312')
    msg['Subject'] = app.config['MAIL_CONTENT']
    msg['Form'] = me
    msg['To'] = recipient
    try:
        print('ahhhhhahahaha')
        s = smtplib.SMTP_SSL(host=app.config['MAIL_SERVER'], port=app.config['MAIL_PORT'])
        s.connect(host=app.config['MAIL_SERVER'], port=app.config['MAIL_PORT'])
        s.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        s.sendmail(me, recipient, msg.as_string())
        s.close()
        print('hahaha')
        return True
    except Exception as e:
        print(str(e))
        print('abc')
        return False
# if __name__ == '__main__':
#     get_user_role()