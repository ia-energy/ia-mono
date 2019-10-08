from flask_restplus import Namespace, Resource, fields
from app.services.auth_0_manager import *
from app.services import test_message_db_srvc as db_srvc

api = Namespace('test_messages', description='test api')

@api.errorhandler(AuthError)
def handle_auth_error(ex):
   response = jsonify(ex.error)
   response.status_code = ex.status_code
   return ex.error, ex.status_code

test_msg = api.model('TestMessage', {
    'uuid': fields.String(required=False, description='Test message identifier'),
    'value': fields.String(required=True, description='Message'),
    'created': fields.String(required=False, description='created timestamp'),
    'updated': fields.String(required=False, description='updated timestamp'),
})

test_msg_pag = api.model('TestMessagePag', {
    'page': fields.Integer(),
    'pages': fields.Integer(),
    'perPage': fields.Integer(),
    'total': fields.Integer(),
    'items': fields.List(fields.Nested(test_msg))
})

@api.route('/')
class TestMessages(Resource):
    @api.doc('get_test_list', params={'page': 'start at x page (1 indexed)', 'perPage': 'how many to return in page'})
    @api.marshal_list_with(test_msg_pag)
    @requires_auth
    def get(self):
        return db_srvc.get_messages(page=int(request.args.get('page', 1)), per_page=int(request.args.get('perPage', 20)))

    @api.doc('post_test')
    @api.marshal_with(test_msg)
    @requires_auth
    def post(self):
        '''Post a test message'''
        content = request.json
        return db_srvc.save_new_msg(content)

@api.route('/<uuid>')
class TestMessage(Resource):
    @api.doc('get_test')
    @api.marshal_with(test_msg)
    @requires_auth
    def get(self, uuid):
        return db_srvc.get_a_message(uuid)

    @api.doc('put_test')
    @api.marshal_with(test_msg)
    @requires_auth
    def put(self, uuid):
        '''Put a test message'''
        content = request.json
        return db_srvc.update_msg(content)
