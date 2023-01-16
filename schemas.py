from marshmallow import Schema, fields


class TagSchema(Schema):
    id = fields.Str(dump_only=True)
    package = fields.Str(required=True)
    version = fields.Str(required=True)
    name = fields.Str(required=True)
    notes = fields.Str()
    created_on = fields.Integer(dump_only=True)
    created_by = fields.Str(dump_only=True)


class TagUpdateSchema(Schema):
    package = fields.Str()
    version = fields.Str()
    name = fields.Str()
    notes = fields.Str()
    created_on = fields.Integer(dump_only=True)
    created_by = fields.Str(dump_only=True)
    updated_on = fields.Integer(dump_only=True)
    updated_by = fields.Str(dump_only=True)
