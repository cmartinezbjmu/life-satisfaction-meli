"""Life satisfaction serializers."""
from marshmallow import Schema, fields
from marshmallow.validate import Range


class LifeSatisfactionInputSchema(Schema):
    """Validate input query params

    Arguments:
        Schema {Schema}

    Returns:
        None
    """
    index_gt = fields.Float(required=True, validate=Range(min=0, max=10))
