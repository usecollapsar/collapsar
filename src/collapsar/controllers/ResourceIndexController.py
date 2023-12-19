"""A ResourceIndexController Module."""
from typing import TYPE_CHECKING
from masonite.controllers import Controller
from masonite.response import Response

from ..helpers.DashboardHelper import DashboardHelper
from ..CollapsarRequest import CollapsarRequest

if TYPE_CHECKING:
    from ..Resource import Resource


class ResourceIndexController(Controller):
    """ResourceIndexController Controller Class."""
    def index(self, request: CollapsarRequest, dashboard_helper: DashboardHelper):
        """Handle resource create request."""

        dashboard_helper.resolve_resource_scripts(request.resource())

        return dashboard_helper.render(
            "resources/ResourceIndex", {"resource": request.param("resource")}
        )

    def handle(self, request: CollapsarRequest, response: Response, resource):
        """Handles main route."""
        resource: "Resource" = request.resource()

        if resource is None:
            return response.json({"success": False})

        data = resource.paginate(request)
        data["meta"]["resource"] = resource.json_serialize()

        return response.json(data)
