import json

from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app import auth0

test_endpoints = Blueprint('test_endpoints', __name__)

@test_endpoints.route('/')
@cross_origin(headers=["Content-Type", "Authorization"])
def up_check():
    return "Flask is up, what's inside!?!"

# This needs authentication
@test_endpoints.route("/api/private-scoped")
@cross_origin(headers=["Content-Type", "Authorization"])
@auth0.requires_auth
def api_private_scoped():
    if auth0.requires_scope("read:private:test"):
        response = "Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this."
        return jsonify(message=response)
    raise AuthError({
        "code": "Unauthorized",
        "description": "You don't have access to this resource"
    }, 403)

# This needs authentication
@test_endpoints.route("/api/private")
@cross_origin(headers=["Content-Type", "Authorization"])
@auth0.requires_auth
def api_private():
    response = "Hello from a private endpoint! You need to be authenticated"
    return jsonify(message=response)
    raise AuthError({
        "code": "Unauthorized",
        "description": "You don't have access to this resource"
    }, 403)

# This needs authentication
@test_endpoints.route("/api/public")
@cross_origin(headers=["Content-Type", "Authorization"])
def api_public():
    response = "Hello from a public endpoint!"
    return jsonify(message=response)
