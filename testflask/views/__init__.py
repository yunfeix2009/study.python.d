from flask import Flask
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import timedelta

app = Flask('flask_final')
# app = Flask('flask_final', template_folder='home_page_templates')

app.secret_key = "1"

app.config.update(
    MAIL_SERVER='smtp.163.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='yunfeix2009@163.com',
    MAIL_PASSWORD='VQXNQTMMGOBHCAAO',
    SQLALCHEMY_ECHO=True,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_DATABASE_URI='mysql://root:123456@127.0.0.1:3306/testdb_orm',
    SECRET_KEY=os.urandom(24),
    PERMANENT_SESSION_LIFETIME=timedelta(days=7),
    log_file_pass='D:\steven'
)


app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
moment = Moment(app)
bootstrap = Bootstrap(app)
mail = Mail(app)

from views.mail_sender import mail_sender
app.register_blueprint(mail_sender, url_prefix='/mail_sender')

from views.guess_num import guess_num
app.register_blueprint(guess_num, url_prefix='/guess_num')

# from final_flask.views.article_publish import article_publish
# app.register_blueprint(article_publish, url_prefix='/article_publish')

# from final_flask.views.message_board import message_board
# app.register_blueprint(message_board, url_prefix='/message_board')

# from final_flask.views import mail_sender_templates
# app.register_blueprint(mail_sender_templates, url_prefix='/mail_sender_templates')

