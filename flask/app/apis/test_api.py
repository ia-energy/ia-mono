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
    'public_id': fields.String(required=False, description='Test message identifier'),
    'value': fields.String(required=True, description='Message'),
    'created': fields.String(required=False, description='created timestamp'),
    'updated': fields.String(required=False, description='updated timestamp'),
})

TEST = [
    {'public_id': '1', 'value': 'message1'},
    {'public_id': '2', 'value': 'message2'},
    {'public_id': '3', 'value': 'message3'},
]


@api.route('/auth_access/', defaults={'public_id': None})
@api.route('/auth_access/<public_id>')
class TestList(Resource):
    @api.doc('list_test')
    @api.marshal_list_with(test)
    @requires_auth
    def get(self, public_id):
        '''List all test'''
        return TEST

    @api.doc('post_test')
    @api.marshal_with(test)
    @requires_auth
    def post(self, public_id):
        '''Post a test message'''
        content = request.json
        return db_srvc.save_new_msg(content)

    @api.doc('put_test')
    @api.marshal_with(test)
    @requires_auth
    def put(self, public_id):
        '''Put a test message'''
        content = request.json
        return db_srvc.update_msg(content)


@api.route('/auth_access/<public_id>')
@api.param('public_id', 'The message identifier')
@api.response(404, 'Test not found')
class Test(Resource):
    @api.doc('get_test')
    @api.marshal_with(test)
    @requires_auth
    def get(self, public_id):
        '''Fetch a test given its identifier'''
        for test in TEST:
            if test['public_id'] == public_id:
                return test
        api.abort(404)


@api.route('/no_auth_access/')
class TestList(Resource):
    @api.doc('list_test')
    @api.marshal_list_with(test)
    def get(self):
        '''List all test'''
        return TEST

@api.route('/no_auth_access/<public_id>')
@api.param('public_id', 'The message identifier')
@api.response(404, 'Test not found')
class Test(Resource):
    @api.doc('get_test')
    @api.marshal_with(test)
    def get(self, public_id):
        '''Fetch a test given its identifier'''
        for test in TEST:
            if test['public_id'] == public_id:
                return test
        api.abort(404)
