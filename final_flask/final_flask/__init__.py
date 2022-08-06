from flask import Flask
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask('flask_final')
app.config.from_pyfile('settings.py')

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
moment = Moment(app)
bootstrap = Bootstrap(app)
mail = Mail(app)

from final_flask.views import mail_sender
app.register_blueprint(mail_sender, url_prefix='/mail_sender')

from final_flask.views import article_publish
app.register_blueprint(article_publish, url_prefix='/article_publish')

from final_flask.views import message_board
app.register_blueprint(message_board, url_prefix='/message_board')

# from final_flask.views import mail_sender
# app.register_blueprint(mail_sender, url_prefix='/mail_sender')

