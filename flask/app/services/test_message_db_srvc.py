import uuid
import datetime
from app import db
from app.model.test_message import TestMessage

def save_new_msg(data):
    print(data)
    msg = TestMessage.query.filter_by(uuid=data['uuid']).first()
    if not msg:
        new_msg = TestMessage(
            uuid=str(uuid.uuid4()),
            value=data['value']
        )
        add(new_msg)
        return new_msg, 201
    return None, 409

def update_msg(data):
    msg = TestMessage.query.filter_by(uuid=data['uuid']).first()
    if not msg:
        return None, 204
    else:
        msg.value = data['value']
        commit()
    return msg, 200

def get_all_messages():
    return test.query.all()

def get_a_message(uuid):
    return test.query.filter_by(uuid=uuid).first()

def add(data):
    db.session.add(data)
    db.session.commit()

def commit():
    db.session.commit()
