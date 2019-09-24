import uuid
import datetime

from app.main import db
from app.main.apis.test_apis import TestMessage


def save_new_msg(data):
    mgs = TestMessage.query.filter_by(public_id=data['public_id']).first()
    if not msg:
        new_mgs = TestMessage(
            public_id=str(uuid.uuid4()),  
            value=data['value'],
            created=datetime.datetime.utcnow()
            updated=datetime.datetime.utcnow()
        )
        save_changes(new_msg)
        response_object = {
             'status': 'success',
              'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
           'status': 'fail',
           'message': 'Msg already exists. Please Log in.',
        }
    return response_object, 409


def get_all_messages():
    return TestMessage.query.all()


def get_a_message(public_id):
    return TestMessage.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
