"""A CollapsarController Module."""
from masonite.views import View
from masonite.controllers import Controller
from masonite.request import Request

from ..helpers.DashboardHelper import DashboardHelper


class CollapsarController(Controller):
    """CollapsarController Controller Class."""

    def index(self, view: View, request: Request):
        """Handle CollapsarController request."""
        dashboard_helper = request.app.make(DashboardHelper)

        return view.render(
            "masonite-collapsar:admin.index", {"dashboard_helper": dashboard_helper}
        )
