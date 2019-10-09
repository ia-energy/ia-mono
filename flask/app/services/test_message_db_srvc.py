import uuid
import datetime
from app import db
from app.model.test_message import TestMessage
from sqlalchemy.sql import func

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
        msg.updated = func.now()
        commit()
    return msg, 200

def get_messages(page,per_page):
    pag = TestMessage.query.paginate(page=page, per_page=per_page, error_out=True, max_per_page=1000)
    return {
      'page' : pag.page,
      'pages' : pag.pages,
      'perPage' : pag.per_page,
      'total' : pag.total,
      'items' : pag.items
    }, 200

def get_a_message(uuid):
    return TestMessage.query.filter_by(uuid=uuid).first()

def add(data):
    db.session.add(data)
    db.session.commit()

def commit():
    db.session.commit()
