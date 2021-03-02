import os

from authlib.integrations.flask_client import OAuth
from flask import Flask, redirect, session, url_for
from flask_cors import CORS
from werkzeug.urls import url_encode

from licmon.core.app import create_app


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
# TODO: Is this the right way to manage CORS?
CORS(app, supports_credentials=True)

# TODO: Remove this...
@app.route('/favicon.ico')
def favicon():
    return '', 200


app.run(port=5000, debug=True)
