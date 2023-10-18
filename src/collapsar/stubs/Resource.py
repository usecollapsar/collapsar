from collapsar import Resource
from collapsar.IdField import IdField
from app.models.__class__ import __class__

class __class__Resource(Resource):
    """__class__ Resource."""

    title = "__class__"
    model = __class__

    @classmethod
    def fields(cls):
        """Return the fields of the resource."""

        return [
            IdField("Id", "id").readonly().sortable(),
        ]
