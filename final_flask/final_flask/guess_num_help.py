import os

room_info_path = "../gasses_dight/room_info.txt"

title = """
<a href="/">首页</a>
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

title_text = """
<h1>欢迎阅读猜数字游戏规则！</h1><br/>
<h3>猜数字游戏由一人创建房间，设置目标数字。向他人分享房间号，<br/>
他人可以加入，开始猜数字游戏。如果猜的数字小了，那么系统会提示你猜的小了；<br/>
然后可以继续猜，如果大了，也会提示你猜的大了，直到猜对为止。</h3>
"""

create_text = """
<h1>请填写房间号和目标数字,目标数字需为整数</h1>
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


def get_info():
    with open(room_info_path, "r", encoding="utf-8") as f:
        info = [i.strip().split("\t") for i in f.readlines()]
        info = dict(info)
    return info


def add_info(room_num, target_num):
    with open(room_info_path, "a+", encoding="utf-8") as f:
        f.write("{}\t{}\n".format(room_num, target_num))



