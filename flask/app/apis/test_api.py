from flask_restplus import Namespace, Resource, fields
from app.services.auth_0_manager import *
from app.services import test_message_db_srvc as db_srvc


api = Namespace('test', description='test api')

@api.errorhandler(AuthError)
def handle_auth_error(ex):
   response = jsonify(ex.error)
   response.status_code = ex.status_code
   return ex.error, ex.status_code


test = api.model('TestMessage', {
    'id': fields.String(required=False, description='Test message identifier'),
    'value': fields.String(required=True, description='Message'),
    'created': fields.String(required=False, description='created timestamp'),
    'updated': fields.String(required=False, description='updated timestamp'),
})

TEST = [
    {'id': '1', 'value': 'message1'},
    {'id': '2', 'value': 'message2'},
    {'id': '3', 'value': 'message3'},
]


@api.route('/auth_access/')
class TestList(Resource):
    @api.doc('list_test')
    @api.marshal_list_with(test)
    @requires_auth
    def get(self):
        '''List all test'''
        return TEST

    @api.doc('post_test')
    @api.marshal_with(test)
    @requires_auth
    def post(self):
        '''Post a test message'''
        content = request.json
        return content


@api.route('/auth_access/<id>')
@api.param('id', 'The message identifier')
@api.response(404, 'Test not found')
class Test(Resource):
    @api.doc('get_test')
    @api.marshal_with(test)
    @requires_auth
    def get(self, id):
        '''Fetch a test given its identifier'''
        for test in TEST:
            if test['id'] == id:
                return test
        api.abort(404)


@api.route('/no_auth_access/')
class TestList(Resource):
    @api.doc('list_test')
    @api.marshal_list_with(test)
    def get(self):
        '''List all test'''
        return TEST

@api.route('/no_auth_access/<id>')
@api.param('id', 'The message identifier')
@api.response(404, 'Test not found')
class Test(Resource):
    @api.doc('get_test')
    @api.marshal_with(test)
    def get(self, id):
        '''Fetch a test given its identifier'''
        for test in TEST:
            if test['id'] == id:
                return test
        api.abort(404)
