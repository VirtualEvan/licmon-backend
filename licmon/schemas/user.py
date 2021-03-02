from marshmallow import fields

from ..core.marshmallow import marshmallow


class UserSchema(marshmallow.Schema):
    username = fields.String()
    name = fields.String()
    email = fields.String()
    # TODO: This needs to be a list of roles, not objects or nested lists
    roles = fields.List(fields.String)
    uid = fields.Integer()
