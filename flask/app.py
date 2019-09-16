from flask import Flask
import json

try:
   with open('ia_flask.json') as config_file:
       data = json.load(config_file)
except FileNotFoundError:
   with open('ia_flask_example.json') as config_file:
       data = json.load(config_file)
  
app = Flask(__name__)

@app.route('/')
def hello_whale():
    return 'Whale, Hello there!'
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
