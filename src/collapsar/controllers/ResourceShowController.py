"""A ResourceShowController Module."""
from typing import TYPE_CHECKING
from masonite.controllers import Controller
from masonite.response import Response
from ..CollapsarRequest import CollapsarRequest
from ..helpers.DashboardHelper import DashboardHelper

if TYPE_CHECKING:
    from ..Resource import Resource


class ResourceShowController(Controller):
    """ResourceShowController Controller Class."""

    def show(self, request: CollapsarRequest, dashboard_helper: DashboardHelper):
        """Handle resource create request."""

        data = self.handle(request)

        return dashboard_helper.render(
            "resources/ResourceShow", {"resource": request.param("resource"), "data": data}
        )

    def handle(
        self, request: CollapsarRequest
    ):
        """Get the fields for the update page."""

        resource: "Resource" = request.resource()
        resource_id = request.param("resource_id")

        if resource is None:
            return None

        model = resource.model.find(resource_id)

        return {
            "data": model.serialize(),
            "resource": resource.json_serialize(),
            "fields": list(
                map(
                    lambda field: field.json_serialize(),
                    resource.show_fields(request),
                )
            ),
        }
