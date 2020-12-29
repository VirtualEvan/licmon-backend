from flask import Blueprint
from flask.views import MethodView

from ..service.product_service import get_product
from ..util.dto import ProductDto


api = Blueprint('api', __name__, url_prefix='/api')
_product = ProductDto.product

# TODO: Separate in different controllers and from api
@api.route('/product/<product_name>')
@api.param('product_name', 'The Product name')
@api.response(404, 'Product not found.')
class Product(MethodView):
    @api.doc('Get usage information about a product')
    @api.marshal_with(_product, skip_none=True)
    def get(self, product_name):
        """Get a product given its name"""
        product = get_product(product_name)
        if not product:
            api.abort(404)
        else:
            return product
