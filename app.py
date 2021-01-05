import os

from flask import Flask
from flask_cors import CORS

# from app import blueprint
from app.main import create_app
from app.main.controller.api import api


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(api)
app.app_context().push()
# TODO: Is this the right way to manage CORS?
CORS(app)

app.run(port=5000, debug=True)
