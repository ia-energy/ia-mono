import uuid
import datetime
from app import db
from app.model.test_message import TestMessage

def save_new_msg(data):
    print(data)
    msg = TestMessage.query.filter_by(public_id=data['public_id']).first()
    if not msg:
        new_msg = TestMessage(
            public_id=str(uuid.uuid4()),
            value=data['value'],
            created=datetime.datetime.utcnow(),
            updated=datetime.datetime.utcnow()
        )
        add(new_msg)
        return new_msg, 201
    return None, 409

def update_msg(data):
    msg = TestMessage.query.filter_by(public_id=data['public_id']).first()
    if not msg:
        return None, 204
    else:
        msg.value = data['value']
        msg.updated = datetime.datetime.utcnow()
        commit()
    return msg, 200

def get_all_messages():
    return test.query.all()

def get_a_message(public_id):
    return test.query.filter_by(public_id=public_id).first()

def add(data):
    db.session.add(data)
    db.session.commit()

def commit():
    db.session.commit()
