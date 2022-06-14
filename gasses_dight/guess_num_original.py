import os
import random
from flask_study.Flask import Flask, request


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
title_text = """<h2>欢迎阅读猜数字游戏规则！<br/>
猜数字游戏由一人创建房间，生成目标数字，另外一人可以加入，
然后开始猜数字游戏，如果猜的数字小了，那么系统会
提示你猜的小了，然后继续猜，
如果大了，也会提示你猜的大了，知道猜对为止。
</h2>"""

app = Flask(__name__)


@app.route("/")
def index():
    """
    猜数字游戏
    主页
    """
    title_text = "<h1>欢迎来到猜数字游戏</h1>\n"
    subtitle_text = "<h3>欢迎来到猜数字游戏</h3>\n"
    content = "如果您想创建一个房间,请点击这个<a href='/create'>创建房间</a>"
    form_content = "<form action='/join' method='post'>\n"
    form_content += "房间号:<input type='text' name='room_num'/>\n"
    form_content += "<button>加入</button></form>"

    return title + title_text + subtitle_text + content + form_content


@app.route("/rule")
def rule():
    return title + title_text


@app.route("/create")
def create_room():
    room_num = str(random.randint(1, 20))
    target_num = str(random.randint(1, 100))
    with open("room_info.txt", "a+", encoding="utf-8") as f:
        f.write("{}\t{}\n".format(room_num, target_num))
    return "房间号:{},目标数字:{}".format(room_num, target_num)


@app.route("/join", methods=["post"])
def join_room():
    room_num = request.form.get("room_num")
    res = os.path.exists("room_info.txt")
    if res:
        with open("room_info.txt", "r", encoding="utf-8") as f:
            info = [i.strip().split("\t") for i in f.readlines()]
            info = dict(info)
            if str(room_num) in info:
                return f'<script>var target = {info[room_num]};{js_code}'
            else:
                return title + "房间号不存在"
    else:
        return title + "房间号不存在，请先创建房间号"


if __name__ == "__main__":
    app.run(debug=True)
