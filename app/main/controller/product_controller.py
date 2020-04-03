from flask import request
from flask_restx import Resource

from ..util.dto import ProductDto
from ..service.product_service import get_product

api = ProductDto.api
_product = ProductDto.product


# @api.route('/')
# class UserList(Resource):
#     @api.doc('list_of_registered_users')
#     @api.marshal_list_with(_user, envelope='data')
#     def get(self):
#         """List all registered users"""
#         return get_all_users()
# 
#     @api.response(201, 'User successfully created.')
#     @api.doc('create a new user')
#     @api.expect(_user, validate=True)
#     def post(self):
#         """Creates a new User """
#         data = request.json
#         return save_new_user(data=data)


@api.route('/<product_name>')
@api.param('product_name', 'The Product name')
@api.response(404, 'Product not found.')
class Product(Resource):
    @api.doc('Get information about a product')
    @api.marshal_with(_product)
    def get(self, product_name):
        """Get a product given its name"""
        product = get_product(product_name)
        if not product:
            api.abort(404)
        else:
            return product