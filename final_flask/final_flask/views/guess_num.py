from flask import session, request, Blueprint, redirect, render_template
from final_flask.guess_num_help import title, title_text, create_text, get_info, add_info, js_code
from final_flask.log_module import logger
guess_num = Blueprint('guess_num', __name__, template_folder='guess_num_templates', static_folder='static')
logger.info()
@guess_num.route("/")
def index():
    if session.get("room"):
        room_num = session.get("room")
        text += f"您已经创建了房间,房间号为:{room_num}"
    else:
        text += "您还未创建房间"
    text += "<h3>欢迎来到猜数字游戏</h3>\n"
    text += "如果您想创建一个房间,请点击这个<a href='/create'>创建房间</a>"
    text += "<form action='/join' method='post'>\n"
    text += "房间号:<input type='text' name='room_num'/>\n"
    text += "<button>加入</button></form>"
    return render_template('index.html')


@guess_num.route("/rule")
def rule():
    return title + title_text


@guess_num.route("/create")
def create_room():
    if session.get("room"):
        return title + f"您已经创建过房间了,房间号是:{session.get('room')}"
    return title + create_text


@guess_num.route("/join", methods=["post"])
def join_room():
    room_num = request.form.get("room_num")
    info = get_info()
    if room_num in info:
        return f'<script>var target = {info[room_num]};{js_code}'
    else:
        return title + "房间号不存在"


@guess_num.route("/check_form", methods=["post"])
def check_form():
    room_num = request.form.get("room_num")
    target_num = request.form.get("target_num")
    if target_num.isdigit():  # and (not session.get("room")):
        info = get_info()
        if room_num in info:
            return title + "房间号已存在,请重新创建房间"
        else:
            add_info(room_num, target_num)
            session["room"] = room_num
            return title + f"创建完毕,房间号:{room_num},目标数字:{target_num}"
    else:
        return title + "目标数字应为整数,请重新创建房间"





@guess_num.after_request
def after_request(response):
    ip = request.remote_addr
    logger.critical('ip: ' + ip + 'entering after_request route in article_publish')
    print('Access to : ' + request.full_path)
    return response


@guess_num.before_request
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
