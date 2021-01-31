from marshmallow import fields

from ..core.marshmallow import marshmallow
from .feature import FeatureSchema


# TODO: Remove fields which are returning null
# TODO: Check the names of the namespaces and models
class ProductSchema(marshmallow.Schema):
    name = fields.String(required=True, description="Product name")
    raw = fields.String(required=True, description="Raw command output")
    features = fields.List(
        fields.Nested(FeatureSchema, skip_none=True),
        required=False,
        description="Product features",
    )
