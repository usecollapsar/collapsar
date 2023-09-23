"""A ResourceStoreController Module."""
import json
from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request


class ResourceStoreController(Controller):
    """ResourceStoreController Controller Class."""

    def handle(self, request: Request, response: Response, resource):
        """Handle resource create request."""

        resource = request.app.make("Collapsar").get_resource(resource)

        if resource is None:
            return response.json({"success": False})

        resource_model = resource.get_model().create(request.all())

        return response.json(
            {"resource_model": json.loads(resource_model.to_json()), "success": True}
        )
