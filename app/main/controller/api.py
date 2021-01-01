from flask import Blueprint, current_app, jsonify
from webargs import flaskparser

# from flask.views import MethodView
from ..schemas.product import ProductSchema
from ..schemas.server import ServerSchema
from ..service.product_service import get_product_info
from ..service.server import get_servers_info


api = Blueprint('api', __name__, url_prefix='/api')

# TODO: Separate in different controllers and from api
@api.route('/product/<product_name>')
# @api.param('product_name', 'The Product name')
# @api.response(404, 'Product not found.')
# class Product(MethodView):
# @api.doc('Get usage information about a product')
# @api.marshal_with(_product, skip_none=True)
def get_product(product_name):
    """Get a product given its name"""
    product = get_product_info(product_name)
    if not product:
        # TODO: Move flaskparser somewhere else
        flaskparser.abort(404)
    else:
        return ProductSchema().jsonify(product)


@api.route('/servers')
# @api.param('product_name', 'The Product name')
# @api.response(404, 'Product not found.')
# class Products(MethodView):
# @api.doc('Get usage information about a product')
# @api.marshal_with(_product, skip_none=True)
def get_servers():
    """Get the lists of products configured"""
    # TODO: Get directly from config??
    # Right now the name of the server is comming inside the objectm rather than as a key
    servers = get_servers_info()
    return ServerSchema(many=True).jsonify(servers)

    
