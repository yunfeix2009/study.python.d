from final_flask.forms import SendForm
from flask import render_template, request, Blueprint
from final_flask import app, mail
from flask_mail import Message
from final_flask.log_module import logger
# mail_sender = Blueprint('mail_sender',__name__)
mail_sender = Blueprint('mail_sender', __name__, template_folder='templates', static_folder='static')
# mail_sender = Blueprint('mail_sender', __name__, template_folder='mail_sender_templates', static_folder='static')

@mail_sender.route('/')
def mainpage():
    logger.critical('entering root route in mail_sender')
    form = SendForm()
    return render_template('mail_sender.html', form=form)

@mail_sender.route('/send', methods=['POST'])
def send_mail():
    logger.critical('entering send route in mail_sender')
    subject = request.form.get('subject')
    to = request.form.get('address')
    body = request.form.get('content')
    name = request.form.get('name')
    address = request.form.get('email_address')
    app.config.update(MAIL_DEFAULT_SENDER=(name, address))
    message = Message(subject, recipients=[to], sender=address, body=body)
    try:
        mail.send(message)
        logger.critical('successfully send a message with '
                        'subject: ' + subject +
                        ', address: ' + to +
                        ', content: ' + name +
                        ', name: ' + address
                        + 'address of sender')
    except Exception as e:
        logger.critical('error when sending' + e)
        return 'failed'
    return 'successed'
