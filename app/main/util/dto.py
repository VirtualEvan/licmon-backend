from flask_restx import Namespace, fields


# TODO: Check the names of the namespaces and models
class ProductDto:
    api = Namespace('Product', description='Product operations')

    license = api.model('license', {
        'username': fields.String(required=True, description='User account'),
        'hostname': fields.String(required=True, description='Host where user is running'),
        'display': fields.String(required=True, description='Display where user is running'),
        'version': fields.String(required=True, description='Version of feature'),
        'server': fields.String(required=True, description='Host where license server is running'),
        'port': fields.String(required=True, description='TCP/IP port where license server is running'),
        'handle': fields.String(required=True, description='License handle'),
        'checkout': fields.String(required=True, description='Time that this license was checked out'),
        'num_licenses': fields.String(required=False, description='Number of licenses the user has')
    })

    feature = api.model('feature', {
        'name': fields.String(required=True, description='Feature name'),
        'version': fields.String(required=False, description='Version number'),
        'vendor': fields.String(required=False, description='Vendor name'),
        'licenses_issued': fields.Integer(required=False, description='Number of licenses issued'),
        'licenses_in_use': fields.Integer(required=False, description='Number of licenses in use'),
        'users': fields.List(fields.Nested(license, skip_none=True), required=False, description='Users using a license'),
        'message': fields.String(required=False, description='Message providing more information')
    })

    product = api.model('product', {
        'name': fields.String(required=True, description='Product name'),
        'features': fields.List(fields.Nested(feature, skip_none=True), required=False, description='Product features')
    })