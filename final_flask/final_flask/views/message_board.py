from flask import flash, redirect, url_for, render_template, request, Blueprint
from final_flask import db
from final_flask.forms import HelloForm
from final_flask.models import Message

massage_board = Blueprint('message_board', __name__, template_folder='templates', static_folder='static')

@massage_board.route('/', methods=['GET', 'POST'])
def message_board():
    print("*" * 30 + 'message_board' + '*' * 30)
    print(Message.timestamp)
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    print(messages)
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Success！Your message have been sent to the world!')
        print("*" * 30 + 'message_board' + '*' * 30)
        return redirect(url_for('message_board.index'))
    print("*" * 30 + 'message_board' + '*' * 30)
    return render_template('message_board.html', form=form, messages=messages)
