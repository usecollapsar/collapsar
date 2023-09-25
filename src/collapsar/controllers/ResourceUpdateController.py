"""A ResourceUpdateController Module."""
import json
from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request


class ResourceUpdateController(Controller):
    """ResourceUpdateController Controller Class."""

    def handle(self, request: Request, response: Response, resource):
        """Handle resource update request."""

        resource = request.app.make("Collapsar").get_resource(resource)

        if resource is None:
            return response.json({"success": False})

        resource_model = resource.get_model().find(request.param("resource_id"))

        resource_model.update(request.all())

        return response.json({"resource": json.loads(resource_model.to_json()), "success": True})
