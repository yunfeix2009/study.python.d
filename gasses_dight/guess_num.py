import os
from flask_study.Flask import Flask, request, session

room_info_path = "room_info.txt"
title = """<a href="/">首页</a>
<a href="/rule">游戏规则</a>
<br/>
"""
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
window.location = "/";
</script>
'''
title_text = """<h1>欢迎阅读猜数字游戏规则！</h1><br/>
<h3>猜数字游戏由一人创建房间，设置目标数字。向他人分享房间号，<br/>
他人可以加入，开始猜数字游戏。如果猜的数字小了，那么系统会提示你猜的小了；<br/>
然后可以继续猜，如果大了，也会提示你猜的大了，直到猜对为止。</h3>"""
create_text = """<h1>请填写房间号和目标数字,目标数字需为整数</h1>
<form action='/check_form' method='post'>
设置房间号:<input type='text' name='room_num'/><br/>
设置目标数字:<input type='text' name='target_num'/>
<button>提交</button>
</form>
"""
if not os.path.exists(room_info_path):
    # 检测是否存在房间信息的文件
    with open(room_info_path, "w", encoding="utf-8") as f:
        pass
app = Flask(__name__)
app.secret_key = os.urandom(24)


def get_info():
    with open(room_info_path, "r", encoding="utf-8") as f:
        info = [i.strip().split("\t") for i in f.readlines()]
        info = dict(info)
    return info


def add_info(room_num, target_num):
    with open(room_info_path, "a+", encoding="utf-8") as f:
        f.write("{}\t{}\n".format(room_num, target_num))


@app.route("/")
def index():
    """
    猜数字游戏
    主页
    """
    text = title + "<h1>欢迎来到猜数字游戏</h1>"
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
    return text


@app.route("/rule")
def rule():
    return title + title_text


@app.route("/create")
def create_room():
    if session.get("room"):
        return title + f"您已经创建过房间了,房间号是:{session.get('room')}"
    return title + create_text


@app.route("/join", methods=["post"])
def join_room():
    room_num = request.form.get("room_num")
    info = get_info()
    if room_num in info:
        return f'<script>var target = {info[room_num]};{js_code}'
    else:
        return title + "房间号不存在"


@app.route("/check_form", methods=["post"])
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


if __name__ == "__main__":
    app.run(debug=True)
