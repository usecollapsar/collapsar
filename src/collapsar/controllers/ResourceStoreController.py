"""A ResourceStoreController Module."""
from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request
from ..Resource import Resource


class ResourceStoreController(Controller):
    """ResourceStoreController Controller Class."""

    def handle(self, request: Request, response: Response, resource):
        """Handle resource create request."""

        resource: Resource = request.app.make("Collapsar").get_resource(resource)

        if resource is None:
            return None

        # this fills every model attribute with request parameters (except id)
        # every field has its own fill method, for example,
        # to Hash the password before assigning it
        [resource_model, callbacks] = resource.fill(request, resource.new_model())
        resource_model.save()

        return response.redirect(
            f"/collapsar/resource/{resource.get_urikey()}/{resource_model.id}"
        ).status(303)
