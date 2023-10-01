from typing import TYPE_CHECKING
from masonite.request import Request
from masonite.foundation import Application

if TYPE_CHECKING:
    from .Resource import Resource


class CollapsarRequest():
    """CollapsarRequest class"""

    def __init__(self, request: Request):
        self.request = request
        self.collapsar = Application().make("Collapsar")

    def resource(self) -> "Resource":
        """Get resource from request"""
        return self.collapsar.get_resource(self.request.params.get("resource"))

    def model(self):
        """Get model from request"""
        return self.resource().model.find(self.request.params.get("resource_id"))
