from marshmallow import fields

from ..core.marshmallow import marshmallow
from .license import LicenseSchema


class FeatureSchema(marshmallow.Schema):
    name = fields.String(required=True, description="Feature name")
    version = fields.String(required=False, description="Version number")
    vendor = fields.String(required=False, description="Vendor name")
    licenses_issued = fields.Integer(
        required=False, description="Number of licenses issued"
    )
    licenses_in_use = fields.Integer(
        required=False, description="Number of licenses in use"
    )
    licenses = fields.List(
        fields.Nested(LicenseSchema, skip_none=True),
        required=False,
        description="Users using a license",
    )
    message = fields.String(
        required=False, description="Message providing more information"
    )
