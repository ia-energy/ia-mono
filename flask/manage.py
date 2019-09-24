import unittest

from flask import Flask
from flask_cors import CORS
#from app.controllers.test_controller import test_endpoints
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.apis import api
from app.apis import blueprint as api1
from app.config import ia_config as config

app = Flask(__name__)
# https://tech.zegami.com/cant-set-authorization-header-for-flask-cors-request-bd88be04fc7c
CORS(app, expose_headers='Authorization')
app.config['DEBUG'] = config['app']['debug']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config['app']['sqlAlchemyDatabaseUri']
app.register_blueprint(api1)
app.app_context().push()
db = SQLAlchemy()
db.init_app(app)

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
   app.run()

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
