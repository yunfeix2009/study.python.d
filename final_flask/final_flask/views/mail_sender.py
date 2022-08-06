from final_flask.forms import SendForm
from flask import render_template, request, Blueprint
from final_flask import app, mail
from flask_mail import Message

massage_board = Blueprint('message_board', __name__, template_folder='templates', static_folder='static')

@massage_board.route('/')
def mainpage():
    print("*" * 30 + 'mailsender' + '*' * 30)
    form = SendForm()
    print("*" * 30 + 'mailsender' + '*' * 30)
    return render_template('mail_sender.html', form=form)

@massage_board.route('/send', methods=['POST'])
def send_mail():
    print("*" * 30 + 'mailsender' + '*' * 30)
    subject = request.form.get('subject')
    to = request.form.get('address')
    body = request.form.get('content')
    name = request.form.get('name')
    address = request.form.get('email_address')
    app.config.update(MAIL_DEFAULT_SENDER=(name, address))
    message = Message(subject, recipients=[to], sender=address, body=body)
    try:
        mail.send(message)
        print("*" * 30 + 'mailsender' + '*' * 30)
    except Exception as e:
        print(str(e))
        print("*" * 30 + 'mailsender' + '*' * 30)
        return 'failed'
    return 'successed'
