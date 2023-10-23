"""A ResourceIndexController Module."""
from typing import TYPE_CHECKING
from masonite.controllers import Controller
from masonite.response import Response
from ..CollapsarRequest import CollapsarRequest

if TYPE_CHECKING:
    from ..Resource import Resource


class ResourceIndexController(Controller):
    """ResourceIndexController Controller Class."""

    def handle(self, collapsar_request: CollapsarRequest, response: Response, resource):
        """Handles main route."""
        resource: "Resource" = collapsar_request.resource()

        if resource is None:
            return response.json({"success": False})

        data = resource.paginate(collapsar_request)
        data["meta"]["resource"] = resource.json_serialize()

        return response.json(data)
