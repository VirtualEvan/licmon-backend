from flask_restplus import Namespace, fields

class ProductDto:
    api = Namespace('product', description='Product operations')
    product = api.model('product', {
        'name': fields.String(required=True, description='Product name'),
        'features': fields.List(required=True, description='Product features')
    })

class FeatureDto:
    api = Namespace('feature', description='Feature operations')
    feature = api.model('feature', {
        'name': fields.String(required=True, description='Feature name'),
        'version': fields.String(required=True, description='Version number'),
        'vendor': fields.String(required=True, description='Vendor name'),
        'licenses_issued': fields.Integer(required=True, description='Number of licenses issued')
        'licenses_in_use': fields.Integer(required=True, description='Number of licenses issued')
        'users': fields.List(required=True, description='Users using a license')
    })

class LicenseDto:
    api = Namespace('license', description='License operations')
    license = api.model('license', {
        'username': fields.String(required=True, description='User account'),
        'hostname': fields.String(required=True, description='Host where user is running'),
        'display': fields.String(required=True, description='Display where user is running'),
        'version': fields.String(required=True, description='Version of feature'),
        'server': fields.String(required=True, description='Host where license server is running'),
        'port': fields.String(required=True, description='TCP/IP port where license server is running'),
        'handle': fields.String(required=True, description='License handle'),
        'checkout': fields.String(required=True, description='Time that this license was checked out'),
    })