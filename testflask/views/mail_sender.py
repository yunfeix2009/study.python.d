from tools.forms import SendForm
from flask import render_template, request, Blueprint, redirect, flash
from views import app, mail
from flask_mail import Message
# from final_flask.log_module import logger
mail_sender = Blueprint('mail_sender', __name__)

@mail_sender.route('/')
def mainpage():
    form = SendForm.SendForm()
    # logger.critical('entering root route in mail_sender_templatplate_folder )
    return render_template('./mail_sender_templates/mail_sender.html', form=form, basepath='/mail_sender/')

@mail_sender.route('/send', methods=['POST'])
def send_mail():
    if request.cookies.get('username') == None:
        print('in')
        return render_template('./home_page_templates/no_permission.html', current_url='发送邮件')
    # logger.critical('entering send route in mail_sender_templates')
    else:
        subject = request.form.get('subject')
        to = request.form.get('address')
        body = request.form.get('content')
        name = request.form.get('name')
        address = app.config['MAIL_USERNAME']
        app.config.update(MAIL_DEFAULT_SENDER=(name, address))
        message = Message(subject, recipients=[to], sender=address, body=body)
        try:
            mail.send(message)
            # logger.critical('successfully send a message with '
            #                 'subject: ' + subject +
            #                 ', address: ' + to +
            #                 ', content: ' + name +
            #                 ', name: ' + address
            #                 + 'address of sender')
        except Exception as e:
            # logger.critical('error when sending' + e)
            flash('发送失败')
            return redirect('/')
        flash('你的信息已被发送')
        return redirect('/')