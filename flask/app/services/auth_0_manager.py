import json
from six.moves.urllib.request import urlopen
from flask import Flask, request, jsonify, _request_ctx_stack
from functools import wraps
from jose import jwt
from app.config import ia_config

# Error handler
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

# Format error response and append status code
def get_token_auth_header():
   print("here get_toke...")
   """Obtains the Access Token from the Authorization Header
   """
   auth = request.headers.get("Authorization", None)
   if not auth:
       raise AuthError({"code": "authorization_header_missing",
                       "description":
                           "Authorization header is expected"}, 401)

   parts = auth.split()

   if parts[0].lower() != "bearer":
       raise AuthError({"code": "invalid_header",
                       "description":
                           "Authorization header must start with"
                           " Bearer"}, 401)
   elif len(parts) == 1:
       raise AuthError({"code": "invalid_header",
                       "description": "Token not found"}, 401)
   elif len(parts) > 2:
       raise AuthError({"code": "invalid_header",
                       "description":
                           "Authorization header must be"
                           " Bearer token"}, 401)

   token = parts[1]
   return token

def requires_auth(f):
   """Determines if the Access Token is valid
   """
   @wraps(f)
   def decorated(*args, **kwargs):
       if validAuth():
           return f(*args, **kwargs)
       raise AuthError({"code": "invalid_header",
           "description": "Unable to find appropriate key"}, 401)
   return decorated

def validAuth():
    token = get_token_auth_header()
    jsonurl = urlopen("https://"+ia_config['auth0']['domain']+"/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ia_config['auth0']['algorithms'],
                audience=ia_config['auth0']['audience'],
                issuer="https://"+ia_config['auth0']['domain']+"/"
            )
        except jwt.ExpiredSignatureError:
            raise AuthError({"code": "token_expired",
                            "description": "token is expired"}, 401)
        except jwt.JWTClaimsError:
            raise AuthError({"code": "invalid_claims",
                         "description":
                                "incorrect claims,"
                                "please check the audience and issuer"}, 401)
        except Exception:
            raise AuthError({"code": "invalid_header",
                            "description":
                                "Unable to parse authentication"
                                " token."}, 401)

        _request_ctx_stack.top.current_user = payload
    return True

def requires_scope(required_scope):
   """Determines if the required scope is present in the Access Token
   Args:
       required_scope (str): The scope required to access the resource
   """
   token = get_token_auth_header()
   unverified_claims = jwt.get_unverified_claims(token)
   print(unverified_claims)
   if unverified_claims.get("scope"):
           token_scopes = unverified_claims["scope"].split()
           for token_scope in token_scopes:
               if token_scope == required_scope:
                   return True
   return False
