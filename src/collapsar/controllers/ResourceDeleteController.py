"""A ResourceDeleteController Module."""
from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request


class ResourceDeleteController(Controller):
    """ResourceDeleteController Controller Class."""

    def handle(self, request: Request, response: Response, resource):
        """Handle resource create request."""

        resource = request.app.make("Collapsar").get_resource(resource)

        if resource is None:
            return response.json({"success": False})

        resource.get_model().find(request.param('resource_id')).delete()

        return response.json(
            {"success": True}
        )
