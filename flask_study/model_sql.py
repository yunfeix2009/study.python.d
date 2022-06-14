from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager


app = Flask(__name__)

app.secret_key = "1"
### 设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/testdb'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

### 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = False

db = SQLAlchemy(app)
manager = Manager(app)


Migrate(app, db)
manager.add_command('db', MigrateCommand)




class Role(db.Model):
    ### 定义表名
    __tablename__ = 'roles'
    ### 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    us = db.relationship('User', backref='role')

    ### repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True)
    pswd = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:%s' % self.name


if __name__ == '__main__':
    ### db.drop_all()
    manager.run()



#迁移的命令流程：
    # python model.py db init
    # python model.py db migrate -m ‘init’
    # python model.py db upgrade