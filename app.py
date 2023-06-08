import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

FLASK_ENV = os.environ['FLASK_ENV']

if FLASK_ENV == 'production':
    app = Flask(__name__, static_folder='build', static_url_path='')
else:
    app = Flask(__name__)

cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/")
def home():
    """Access production build.

    This is needed in order to access the production build
    on the server.
    """
    if FLASK_ENV == 'production':
        print('Using the production build!')
        return send_from_directory(app.static_folder, 'index.html')

@app.route("/example")
def example():
    return jsonify("Hello from python!")
