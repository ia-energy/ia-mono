import json

from flask import Flask, request, jsonify
from flask_cors import cross_origin
from app.controllers.test_controller import test_endpoints

from app.config import ia_config

app = Flask(__name__)
app.register_blueprint(test_endpoints)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
