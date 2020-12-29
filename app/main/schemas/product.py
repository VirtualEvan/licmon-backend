from marshmallow import fields
from .core.marshmallow import marshmallow


# TODO: Check the names of the namespaces and models
class ProductSchema(marshmallow.schema):
    name = fields.String(required=True, description='Product name')
    features = fields.List(
        fields.Nested(feature, skip_none=True),
        required=False,
        description='Product features',
    )
