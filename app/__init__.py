# app/__init__.py

from flask import Blueprint
from flask_restx import Api

from .main.controller.product_controller import api as product_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTX API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restx web service'
          )

api.add_namespace(product_ns, path='/product')