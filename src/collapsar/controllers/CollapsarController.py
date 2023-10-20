"""A CollapsarController Module."""
import os
from masonite.views import View
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from ..helpers.DashboardHelper import DashboardHelper


class CollapsarController(Controller):
    """CollapsarController Controller Class."""

    def index(self, view: View, request: Request):
        """Handle CollapsarController request."""
        dashboard_helper = request.app.make(DashboardHelper)

        return view.render(
            "collapsar:admin.index", {"dashboard_helper": dashboard_helper}
        )

    def get_js(self, response: Response):
        """Return the JS file."""
        return response.download("app.js", self.get_asset("app-bundle.umd.js"))

    def get_css(self, response: Response):
        """Return the css file."""
        return response.download("style.css", self.get_asset("style.css"))

    def get_asset(self, filename):
        """Return file path."""
        return os.path.dirname(__file__) + "/../dist/assets/" + filename
