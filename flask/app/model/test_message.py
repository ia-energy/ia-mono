from app import db
from sqlalchemy.sql import func

class TestMessage(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "test_messages"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uuid = db.Column(db.String(256), unique=True, nullable=False)
    value = db.Column(db.String(2000), unique=False, nullable=False)
    created = db.Column(db.DateTime, default=func.now())
    updated = db.Column(db.DateTime, onupdate=func.now())

    def __repr__(self):
        return "<TestMessage '{}'>".format(self.uuid)
