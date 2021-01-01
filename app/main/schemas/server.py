from marshmallow import fields
from ..core.marshmallow import marshmallow


class ServerSchema(marshmallow.Schema):
    name = fields.String(required=True, description="Name of the licensed product")
    port = fields.Integer(
        required=True, description="Port where the license server is running"
    )
    hostnames = fields.List(
        fields.String, required=True, description="List of aliases and server names"
    )
