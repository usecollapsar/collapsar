"""A ResourceUpdateController Module."""
import json
from masonite.controllers import Controller
from masonite.response import Response

from ..controllers.ResourceShowController import ResourceShowController
from ..helpers.DashboardHelper import DashboardHelper
from ..CollapsarRequest import CollapsarRequest


class ResourceUpdateController(Controller):
    """ResourceUpdateController Controller Class."""

    def edit(self, request: CollapsarRequest, dashboard_helper: DashboardHelper):
        """Handle resource create request."""

        data = ResourceShowController().handle(request)

        return dashboard_helper.render(
            "resources/ResourceEdit", {"resource": request.param("resource"), "data": data}
        )

    def create(self, request: CollapsarRequest, dashboard_helper: DashboardHelper):
        """Handle resource create request."""

        resource = request.resource()

        if resource is None:
            return None

        fields = list(map(lambda field: field.json_serialize(), resource.creation_fields()))

        data = {
            "isCreating": True,
            "fields": fields,
        }

        return dashboard_helper.render(
            "resources/ResourceEdit", {"resource": request.param("resource"), "data": data}
        )

    def handle(self, request: CollapsarRequest, response: Response):
        """Handle resource update request."""

        resource = request.resource()

        if resource is None:
            return None

        resource_model = resource.get_model().find(request.param("resource_id"))

        [resource_model, callbacks] = resource.fill(request, resource_model)
        resource_model.save()

        return response.redirect(
            f"/collapsar/resource/{request.param('resource')}/{resource_model.id}"
        ).status(303)
