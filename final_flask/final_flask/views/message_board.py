from flask import flash, redirect, url_for, render_template, request, Blueprint
from final_flask import db
from final_flask.forms import HelloForm
from final_flask.models import Message
from final_flask.log_module import logger

massage_board = Blueprint('message_board', __name__, template_folder='message_board_templates', static_folder='static')

@massage_board.route('/', methods=['GET', 'POST'])
def message_board():
    logger.critical("*" * 30 + 'message_board' + '*' * 30)
    logger.critical('timestamp:' + Message.timestamp)
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    logger.critical('messages:' + messages)
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Success！Your message have been sent to the world!')
        return redirect(url_for('message_board.index'))
    return render_template('message_board.html', form=form, messages=messages)


