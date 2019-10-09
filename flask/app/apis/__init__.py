from flask_restplus import Api
from app.services.auth_0_manager import AuthError
from .test_api import api as ns1
from flask import Blueprint

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

blueprint = Blueprint('api', __name__, url_prefix='/api/1')

api = Api(
    blueprint,
    title='IA API',
    version='1.0',
    description='RESTFUL API for IA webclient',
    security='Bearer Auth', authorizations=authorizations,
    # All API metadatas
)


api.add_namespace(ns1)
