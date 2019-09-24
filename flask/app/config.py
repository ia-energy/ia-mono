import os
import sys
import json

basedir = os.path.dirname(os.path.realpath(sys.argv[0]))

try:
   ia_config
except NameError:
   try:
      with open(basedir + '/ia_flask.json') as config_file:
         ia_config = json.load(config_file)
   except FileNotFoundError:
         with open(basedir + '/ia_flask_example.json') as config_file:
            ia_config= json.load(config_file)
