from views import db


class Message(db.Model):
    room_num = db.Column(db.Integer(), primary_key=True)
    target_num = db.Column(db.Integer())