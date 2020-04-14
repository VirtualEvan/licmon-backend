from flask import request
from flask_restx import Resource

from ..util.dto import ProductDto
from ..service.product_service import get_product

api = ProductDto.api
_product = ProductDto.product

@api.route('/<product_name>')
@api.param('product_name', 'The Product name')
@api.response(404, 'Product not found.')
class Product(Resource):
    @api.doc('Get usage information about a product')
    @api.marshal_with(_product, skip_none=True)
    def get(self, product_name):
        '''Get a product given its name'''
        product = get_product(product_name)
        if not product:
            api.abort(404)
        else:
            return product