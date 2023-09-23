"""A ResourceShowController Module."""
from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request


class ResourceShowController(Controller):
    """ResourceShowController Controller Class."""

    def handle(self, request: Request, response: Response, resource, resource_id):
        """Get the fields for the update page."""

        resource = request.app.make("Collapsar").get_resource(resource)

        if resource is None:
            return response.json({"success": False})

        model = resource.model.find(resource_id)

        return response.json(
            {
                "data": model.serialize(),
                "resource": resource.json_serialize(),
                "fields": list(map(lambda resource: resource.json_serialize(), resource.show_fields())),
            }
        )
