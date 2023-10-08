"""A FieldsController Module."""
from masonite.controllers import Controller
from masonite.response import Response
from ..CollapsarRequest import CollapsarRequest
from ..Resource import Resource


class FieldsController(Controller):
    """FieldsController Controller Class."""

    def creation(self, collapsar_request: CollapsarRequest, response: Response, resource):
        """Get the fields for the creation form."""
        resource: "Resource" = collapsar_request.resource()

        if resource is None:
            return response.json({'success': False})

        fields = list(map(lambda field: field.json_serialize(), resource.creation_fields()))

        return response.json({
            'fields': fields
        })
