from final_flask.forms import SendForm
from flask import render_template, request, Blueprint, redirect
from final_flask import app, mail
from flask_mail import Message
from final_flask.log_module import logger
main_page = Blueprint('mail_sender', __name__, template_folder='main_page_templates', static_folder='static')

@main_page.after_request
def after_request(response):
    ip = request.remote_addr
    logger.critical('ip: ' + ip + 'entering after_request route in article_publish')
    print('Access to : ' + request.full_path)
    return response


@main_page.before_request
def before_request():
    username = session.get('username')
    if request.path != "/login":
        if request.path == "/":
            pass
        elif request.path == "/homepage":
            pass
        elif request.path == "/join":
            pass
        elif request.path == "/save_usr":
            pass
        elif username == None or session.get(username) != 'success':
            return redirect("/")
