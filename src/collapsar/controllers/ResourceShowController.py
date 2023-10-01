"""A ResourceShowController Module."""
from typing import TYPE_CHECKING
from masonite.controllers import Controller
from masonite.response import Response
from ..CollapsarRequest import CollapsarRequest

if TYPE_CHECKING:
    from ..Resource import Resource


class ResourceShowController(Controller):
    """ResourceShowController Controller Class."""

    def handle(
        self, collapsar_request: CollapsarRequest, response: Response, resource, resource_id
    ):
        """Get the fields for the update page."""

        resource: "Resource" = collapsar_request.resource()

        if resource is None:
            return response.json({"success": False})

        model = resource.model.find(resource_id)

        return response.json(
            {
                "data": model.serialize(),
                "resource": resource.json_serialize(),
                "fields": list(
                    map(
                        lambda field: field.json_serialize(),
                        resource.show_fields(collapsar_request),
                    )
                ),
            }
        )
