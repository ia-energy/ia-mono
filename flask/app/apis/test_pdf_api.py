from flask_restplus import Namespace, Resource, fields
from app.services.auth_0_manager import *
from flask import Response
from app import s3

api = Namespace('test_pdf', description='test pdf api')

@api.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return ex.error, ex.status_code

@api.route('/<name>')
class PDF(Resource):
    @api.doc('get_test')
    @api.produces(["application/pdf"])
    def get(self, name):
        if not name.endswith(".pdf"):
            raise Execption("Request not for PDF")
        file = s3.get_object(Bucket='ia-energy-rob-test-bucket',Key='test/' + name)
        return Response(
            file['Body'].read(),
            mimetype='application/pdf',
            headers={"Content-Disposition": "attachment;filename="+name})
