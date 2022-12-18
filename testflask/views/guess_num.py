from flask import session, request, Blueprint, render_template
from tools.log_module import logger
from tools.models import sql
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
    sql.close(conn, cur)
    info = {}
    for i in info_tuple:
        info[str(i[0])] = str(i[1])
    return info

def get_room_num():
    conn, cur = sql.get_conn()
    room_num_query = 'select room_num from guess_num'
    room_num_tuple = sql.query(cur, room_num_query)
    sql.close(conn, cur)
    room_num = []
    for i in room_num_tuple:
        room_num.append(i[0])
    return room_num


def add_info(room_num, target_num):
    conn, cur = sql.get_conn()
    add_sql = 'insert into guess_num(room_num, target_num) values(' + room_num + ',' + target_num + ')'
    sql.normal_ex(conn, cur, add_sql)
    sql.close(conn, cur)



@guess_num.route("/")
def index():
    logger.info(guess_num)
    return render_template('./guess_num_templates/have_room.html', basepath=basepath)


@guess_num.route("/rule")
def rule():
    return render_template('guess_num_templates/rules.html', basepath=basepath)

@guess_num.route("/view_room_num")
def view_room_num():
    room_num = get_room_num()
    return render_template('guess_num_templates/view_room_num.html', basepath=basepath, room_num=room_num)


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
    logger.critical('now entering....')
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
