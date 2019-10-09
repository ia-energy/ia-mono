import unittest

from flask import Flask, redirect
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import db
from app.config import ia_config as config
from app.apis import api
from app.apis import blueprint as api1

app = Flask(__name__)
# https://tech.zegami.com/cant-set-authorization-header-for-flask-cors-request-bd88be04fc7c
CORS(app, expose_headers='Authorization')
app.register_blueprint(api1)
app.app_context().push()
app.config['DEBUG'] = config['app']['debug']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config['app']['sqlAlchemyDatabaseUri']
manager = Manager(app)

db.init_app(app)
# DB model imports
from app.model.test_message import TestMessage
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@app.route("/")
@app.route("/api")
def index():
    return redirect('/api/1/')

@manager.command
def run():
   app.run(debug=True, host='0.0.0.0')

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='*test.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
                return 0
    return 1

if __name__ == '__main__':
    manager.run()
