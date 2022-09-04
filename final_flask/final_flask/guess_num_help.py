import os

room_info_path = "../gasses_dight/room_info.txt"

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



