from flask import Blueprint, current_app, jsonify
from webargs import flaskparser

# from flask.views import MethodView
from ..schemas.product import ProductSchema
from ..service.product_service import get_product_info


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


@api.route('/products')
# @api.param('product_name', 'The Product name')
# @api.response(404, 'Product not found.')
# class Products(MethodView):
# @api.doc('Get usage information about a product')
# @api.marshal_with(_product, skip_none=True)
def get_products():
    """Get the lists of products configured"""
    return jsonify(current_app.config['SERVER_LIST'])
