import json

from flask import Flask, request, jsonify
from flask_cors import cross_origin

from app.services.auth_0_manager import Auth0Manager

try:
   with open('ia_flask.json') as config_file:
       config = json.load(config_file)
except FileNotFoundError:
   with open('ia_flask_example.json') as config_file:
       config= json.load(config_file)

app = Flask(__name__)

auth0 = Auth0Manager(config['Auth0']['domain'], config['Auth0']['audience'])

@app.route('/')
@cross_origin(headers=["Content-Type", "Authorization"])
def up_check():
    return "Flask is up, what's inside!?!"

# This needs authentication
@app.route("/api/private-scoped")
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
@app.route("/api/private")
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
@app.route("/api/public")
@cross_origin(headers=["Content-Type", "Authorization"])
def api_public():
    response = "Hello from a public endpoint!"
    return jsonify(message=response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
