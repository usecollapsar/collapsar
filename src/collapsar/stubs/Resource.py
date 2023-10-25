from collapsar import Resource
from collapsar.Id import Id
from app.models.__class__ import __class__


class __class__Resource(Resource):
    """__class__ Resource."""

    title = "__class__"
    model = __class__

    @classmethod
    def fields(cls):
        """Return the fields of the resource."""

        return [
            Id("Id", "id").readonly().sortable(),
        ]
