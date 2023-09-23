"""A FieldsController Module."""
from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request


class FieldsController(Controller):
    """FieldsController Controller Class."""

    def index(self, request: Request, response: Response, resource):
        """Get the fields for the index page."""

    def creation(self, request: Request, response: Response, resource):
        """Get the fields for the creation form."""
        resource = request.app.make('Collapsar').get_resource(resource)

        if resource is None:
            return response.json({'success': False})

        fields = list(map(lambda field: field.json_serialize(), resource.creation_fields()))

        return response.json({
            'fields': fields
        })

    def update(self, request: Request, response: Response, resource):
        """Get the fields for the update page."""
