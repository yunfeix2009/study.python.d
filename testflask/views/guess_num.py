from flask import session, request, Blueprint, render_template
from tools.log_module import logger
from tools.models import sql
import os
guess_num = Blueprint('guess_num', __name__, template_folder='templates')

basepath = '/guess_num/'

js_code = '''
var current = undefined;
var cancelled = false;
while(target != current ){
    current = prompt("请输入你猜的数字");
    if(!current){
        cancelled = true;
        break;
    }
    if(current < target){
        alert('你猜的数字太小了！'); 
        continue;
    }
    if(current > target){
        alert('你猜的数字太大了！');
        continue;
    }
}
if(!cancelled){
    alert('你真厉害，猜中了！');
}
window.location = "/guess_num";
</script>
'''



def get_info():
    conn, cur = sql.get_conn()
    info_query = 'select room_num, target_num from guess_num'
    info_tuple = sql.query(cur, info_query)
    info = {}
    for i in info_tuple:
        info[str(i[0])] = str(i[1])
    return info


def add_info(room_num, target_num):
    conn, cur = sql.get_conn()
    add_sql = 'insert into guess_num(room_num, target_num) values(' + room_num + ',' + target_num + ')'
    sql.normal_ex(conn, cur, add_sql)



@guess_num.route("/")
def index():
    logger.info(guess_num)
    return render_template('./guess_num_templates/have_room.html', basepath=basepath)


@guess_num.route("/rule")
def rule():
    return render_template('guess_num_templates/rules.html', basepath=basepath)


@guess_num.route("/create")
def create_room():
    if session.get("room"):
        return render_template('guess_num_templates/exist_room.html', room_num=session.get("room"), basepath=basepath)
    return render_template('guess_num_templates/create_room.html', basepath=basepath)


@guess_num.route("/join", methods=["post"])
def join_room():
    room_num = request.form.get("room_num")
    info = get_info()
    if room_num in info:
        logger.critical(f'<script>var target = {info[room_num]};{js_code}')
        return f'<script>var target = {info[room_num]};{js_code}'
    else:
        return render_template('guess_num_templates/no_exist_room.html', basepath=basepath)


@guess_num.route("/check_form", methods=["post"])
def check_form():
    room_num = request.form.get("room_num")
    target_num = request.form.get("target_num")
    if target_num.isdigit():
        info = get_info()
        if room_num in info:
            return render_template('guess_num_templates/recreate_room.html', basepath=basepath)
        else:

            add_info(room_num, target_num)
            session["room"] = room_num
            return render_template('guess_num_templates/successfully_create.html', room_num=room_num, target_num=target_num, basepath=basepath)
    else:
        return render_template('guess_num_templates/recreate_room_2.html', basepath=basepath)





# @guess_num.after_request
# def after_request(response):
#     ip = request.remote_addr
#     logger.critical('ip: ' + ip + 'entering after_request route in article_publish')
#     print('Access to : ' + request.full_path)
#     return response
#
#
# @guess_num.before_request
# def before_request():
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
