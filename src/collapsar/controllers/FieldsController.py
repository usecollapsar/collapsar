"""A FieldsController Module."""
from masonite.controllers import Controller
from masonite.response import Response
from ..CollapsarRequest import CollapsarRequest
from ..Resource import Resource


class FieldsController(Controller):
    """FieldsController Controller Class."""

    def get_scripts(self, request: CollapsarRequest, response: Response):
        """Get the scripts for the given resource."""
        script = request.input("script")
        file_path = request.app.make("Collapsar").get_script(script)

        return response.file(file_path)

    def creation(self, collapsar_request: CollapsarRequest, response: Response, resource):
        """Get the fields for the creation form."""
        resource: "Resource" = collapsar_request.resource()

        if resource is None:
            return response.json({'success': False})

        fields = list(map(lambda field: field.json_serialize(), resource.creation_fields()))

        return response.json({
            'fields': fields
        })
