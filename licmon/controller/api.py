from flask import Blueprint, current_app, jsonify, request
from webargs import flaskparser
from werkzeug.exceptions import TooManyRequests

from licmon.core.auth import allow_anonymous
from licmon.core.limiter import limiter
from licmon.core.notifications import send_email

# from flask.views import MethodView
from ..schemas.product import ProductSchema
from ..schemas.server import ServerSchema
from ..service.product import get_product_info
from ..service.server import get_servers_info


api = Blueprint('api', __name__, url_prefix='/api')


@api.errorhandler(TooManyRequests)
def _ratelimit_handler(e):
    return jsonify(error=f'ratelimit exceeded {e.description}'), 429


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


# TODO: Move this to a features controller
# TODO: All restrictions could be ignored by admins
# A function checking if this option is enabled and if the user is admin
# could be added as a `exempt_when=lambda: current_user.is_admin`
@api.route('/request-release/<product_name>/<feature_name>', methods=('POST',))
# TODO: Should be restricted to logged in users
@allow_anonymous
# TODO: This doesn't seem like an elegant solution
@limiter.limit(
    lambda: current_app.config['EMAIL_COOLDOWN'],
    lambda: f"{request.view_args.get('product_name')}.{request.view_args.get('feature_name')}",
)
def request_release(product_name, feature_name):
    # TODO: get feature instead of the whole product
    product = get_product_info(product_name)
    if not product:
        # TODO: Move flaskparser somewhere else
        flaskparser.abort(404)

    # TODO: Do this in a nicer way, using a feature shoud improve the solution
    # TODO: The domain should not be hardcoded
    feature = next((f for f in product.features if f.name == feature_name), None)
    user_emails = set(map(lambda l: f'{l.username}@cern.ch', feature.licenses))
    send_email(
        f'PLEASE NOTE! - All {product_name} licences for {feature_name} taken!',
        'release_email.txt',
        'release_email.html',
        {
            'product': product_name,
            'feature': feature_name,
        },
        user_emails,
    )
    return '', 204
