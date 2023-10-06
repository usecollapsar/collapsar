from typing import TYPE_CHECKING
from masonite.request import Request
from masonite.foundation import Application
from .traits.ForwardsCalls import ForwardsCalls

if TYPE_CHECKING:
    from .Resource import Resource


class CollapsarRequest(ForwardsCalls):
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

    def validate(self, rules):
        """Validate request"""

    def __getattr__(self, name):
        if hasattr(self.request, name):
            return getattr(self.request, name)

        return self.forwards_call_to(self.request, name)
