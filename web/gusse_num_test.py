import random,os
from flask import Flask,request,redirect,url_for
from flask import session

app = Flask(__name__)
app.secret_key = os.urandom(24)
hacker = False
dict_room_target = {}
list_room = []
dict = {'username':'root','pwd':'123'}

@app.route('/')
def hello():
    success = request.args.get("success")
    if success=='1' :
        return redirect("gusse_num_mainpage")
    else :
        return f"<h1>请登录</h1><br><a href='/login'> 点这登录 </a>"

@app.route('/login')
def commit():
    global hacker
    if hacker == True:
        hacker = False
        return redirect("/trickhacker")
    return '<form action="/submit" method="get">  ' \
           'User Name: <input type="text" name="username" value="">  ' \
           '<br>'\
           'Password: <input type="password" name="pwd" value="">  ' \
           '<br>'\
           '<input type="submit" value="提交">  ' \
           '</form>'

@app.route('/submit')
def submit1():
    username = request.args.get("username")
    password = request.args.get("pwd")
    session['username'] = username
    if username == dict['username'] and password == dict['pwd']:
        print('success')
        session[username] = "success"
        return redirect('/?success=1&abc=6')
    else:
        print('failed')
        return redirect("login")

@app.route("/gusse_num_mainpage")
def index():
    return '''
    <a href="/gusse_num_mainpage">首页<a/>
    <a href="/rule">游戏规则</a>
    <h1>欢迎您来到猜数字游戏</h1>
    <h3>如果您想创建一个房间，请点击这个<a href="/create">创建房间</a></h3>
    <form action="/join" method="GET">
    房间号:<input type="text" name="room_num"/>
    <input type='submit' value='加入'/>
    <br/>
    <a href="/redirect">别点我</a>
    </form>'''

@app.route("/rule")
def game_rule():
    return '''
    <a href="/gusse_num_mainpage">首页<a/>
    <h2>欢迎阅读猜数字游戏规则！<br/>猜数字游戏由一人创建房间，生成目标数字，另外一人可以加入，然后开始猜数字游戏，如果猜的数字小了，那么系统会提示你猜的小了，如果大了，那么系统会提示你猜的大了，直到游戏结束。</h2>
    '''

@app.route("/redirectToTrick")
def to_trick():
    trick_url = url_for('trick')
    return redirect(trick_url)

@app.route("/trick")
def trick():
    return "<h1>谁让你点的，回不去了吧，你就待着吧<h1/></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br><h5> <h5/><a href='/gusse_num_mainpage'>.<a/>"

@app.route("/trickhacker")
def trick_hacker():
    return "<h1>听我句劝，别搞这些有的没的<br/>don't do that again<h1/></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br><h5> <h5/><a href='/login'>.<a/>"

@app.route("/create")
def create_room():
    room_num = str(random.randint(1,20))
    if room_num not in list_room:
        list_room.append(room_num)
    else:
        str_list_room = str(list_room)
        return '''
                <h1>房间号已存在
                </br>
                请重新创建
                </br></h1>
                已创建了''' + str_list_room + '''<a href="/gusse_num_mainpage">确定</a>
                '''
    target_num = str(random.randint(1,100))
    room_target_num = room_num + " " + target_num
    with open("room_tar.txt","a",encoding="utf-8") as f:
        f.write(room_target_num + "\n")
    return "房间号为:"+room_num+"<br/>目标数字为:"+ target_num+"<br/><a href='/gusse_num_mainpage?'room_num="+room_num+"target_num="+room_num+">首页<a/>"

@app.route("/join", methods=["post","get"])
def join():
    room_number = request.args.get("room_num")
    print(room_number)
    res = os.path.exists("room_tar.txt")
    if res:
        with open("room_tar.txt", "r") as f:
            while True:
                room_tar_data = f.readline().replace("\n", "")
                if room_tar_data:
                    list1 = room_tar_data.split(" ")
                    x, y = list1[0], list1[1]
                    if room_number == x:
                        return '''
                                <script>
                                    var target = ''' + y + ''';
                                    var current = undefined;
                                    var cancelled = false;
                                    while(target!=current){
                                        current = prompt("请输入你猜的数字")
                                        if(!current){
                                            cancelled = true;
                                            alert(current)
                                            alert("再玩就玩坏了!!!");
                                            break;
                                        }
                                        if(current<target){
                                            alert("你猜的数字太小了");
                                        }
                                        if(current>target){
                                            alert("你猜的数字太大了");
                                        }
                                    }
                                        if(!cancelled){
                                            alert("你真厉害，猜中了");
                                        }
                                    window.location = "/gusse_num_mainpage";
                                </script>
                            '''
                else:
                    return '<a href="/gusse_num_mainpage">首页<a/>房间号不存在，请先创建房间号'

@app.after_request
def after_request(response):
    print('Access to : ' + request.full_path )
    return response

@app.before_request
def before_request():
    username = session.get('username')
    if request.path != "/login" :
        if request.path == "/submit":
            pass
        elif request.path == "/":
            pass
        elif request.path == "/trickhacker":
            pass
        elif username == None or session.get(username) != 'success':
            hacker = True
            return redirect("/login")

if __name__ == '__main__':
    app.run(debug=True)