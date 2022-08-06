from final_flask import app
import os
from datetime import timedelta
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
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
)
