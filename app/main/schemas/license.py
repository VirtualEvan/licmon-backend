from marshmallow import fields

from ..core.marshmallow import marshmallow


class LicenseSchema(marshmallow.Schema):
    username = fields.String(required=True, description="User account")
    hostname = fields.String(required=True, description="Host where user is running")
    display = fields.String(required=True, description="Display where user is running")
    version = fields.String(required=True, description="Version of feature")
    server = fields.String(
        required=True, description="Host where license server is running"
    )
    port = fields.String(
        required=True, description="TCP/IP port where license server is running"
    )
    handle = fields.String(required=True, description="License handle")
    checkout = fields.String(
        required=True, description="Time that this license was checked out"
    )
    num_licenses = fields.String(
        required=False, description="Number of licenses the user has"
    )
