from flask import session, request, Blueprint, redirect, render_template
from tools.log_module import logger
import os
guess_num = Blueprint('guess_num', __name__, template_folder='templates')
# guess_num = Blueprint('guess_num', __name__, template_folder='mail_sender_templates', static_folder='static')


room_info_path = "room_info.txt"

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


if not os.path.exists(room_info_path):
    # 检测是否存在房间信息的文件
    with open(room_info_path, "w", encoding="utf-8") as f:
        pass


def get_info():
    with open(room_info_path, "r", encoding="utf-8") as f:
        info = [i.strip().split("\t") for i in f.readlines()]
        info = dict(info)
    return info


def add_info(room_num, target_num):
    with open(room_info_path, "a+", encoding="utf-8") as f:
        f.write("{}\t{}\n".format(room_num, target_num))




@guess_num.route("/")
def index():
    logger.info(guess_num)
    if session.get("room"):
        room_num = session.get("room")
        return render_template('./guess_num_templates/have_room.html', room_num=room_num, basepath='/guess_num/')
    else:
        return render_template('./guess_num_templates/no_room.html', basepath='/guess_num/')


@guess_num.route("/rule")
def rule():
    return render_template('guess_num_templates/rules.html', basepath='/guess_num/')


@guess_num.route("/create")
def create_room():
    if session.get("room"):
        return render_template('guess_num_templates/exist_room.html', room_num=session.get("room"), basepath='/guess_num/')
    return render_template('guess_num_templates/create_room.html', basepath='/guess_num/')


@guess_num.route("/join", methods=["post"])
def join_room():
    room_num = request.form.get("room_num")
    info = get_info()
    if room_num in info:
        logger.critical(f'<script>var target = {info[room_num]};{js_code}')
        return f'<script>var target = {info[room_num]};{js_code}'
    else:
        return render_template('guess_num_templates/no_exist_room.html', basepath='/guess_num/')


@guess_num.route("/check_form", methods=["post"])
def check_form():
    room_num = request.form.get("room_num")
    target_num = request.form.get("target_num")
    if target_num.isdigit():  # and (not session.get("room")):
        info = get_info()
        if room_num in info:
            return render_template('guess_num_templates/recreate_room.html', basepath='/guess_num/')
        else:
            add_info(room_num, target_num)
            session["room"] = room_num
            return render_template('guess_num_templates/successfully_create.html', room_num=room_num, target_num=target_num, basepath='/guess_num/')
    else:
        return render_template('guess_num_templates/recreate_room_2.html', basepath='/guess_num/')





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
