from .. import db, flask_bcrypt

class TestMessage(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "test_messages"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.String(2000), unique=True, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<TestMessage '{}'>".format(self.username)
