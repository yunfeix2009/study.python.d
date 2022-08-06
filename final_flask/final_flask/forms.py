from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()


class SendForm(FlaskForm):
    subject = StringField('email subject:', validators=[DataRequired(), Length(1,50)])
    address = StringField('email address', validators=[DataRequired(), Length(1, 50)])
    content = TextAreaField('email', validators=[DataRequired(), Length(1, 500)])
    name = StringField('your name', validators=[DataRequired(), Length(1, 50)])
    email_address = StringField('your email address', validators=[DataRequired(), Length(1, 50)])
    submit = SubmitField()


class RegisterForm(FlaskForm):
    us = StringField(label=u'用户',
                     validators=[DataRequired(message='用户名不能为空...'),
                                 Length(min=2, max=12, message='长度为2-12位')],
                     render_kw={'placeholder': '请输入用户名...'})
    ps = PasswordField(label=u'密码',
                       validators=[DataRequired(message='密码不能为空...'),
                                   Length(min=6, max=12, message='长度为6-12位'),
                                   EqualTo('ps2', message='密码不一致')],
                       render_kw={'placeholder': '请输入密码...'})
    ps2 = PasswordField(label=u'确认密码',
                        validators=[DataRequired(message='密码不能为空...'),
                                    Length(min=6, max=12, message='长度为6-12位'), ],
                        render_kw={'placeholder': '请输入密码...'})
    alias = StringField(label=u'笔名',
                        validators=[DataRequired(message='笔名不能为空...'),
                                    Length(max=100, message='别乱来'), ],
                        render_kw={'placeholder': '请输入笔名...'})
    submit = SubmitField(u'提交')

