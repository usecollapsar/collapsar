"""A CollapsarController Module."""
import os
from masonite.views import View
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response


class CollapsarController(Controller):
    """CollapsarController Controller Class."""

    def index(self, view: View):
        """Handle CollapsarController request."""
        return view.render("collapsar:admin.index")

    def get_js(self, response: Response):
        """Return the JS file."""
        return response.download("app.js", self.get_asset("app-bundle.umd.js"))

    def get_css(self, response: Response):
        """Return the css file."""
        return response.download("style.css", self.get_asset("style.css"))

    def get_asset(self, filename):
        """Return file path."""
        return os.path.dirname(__file__) + "/../dist/assets/" + filename

    def get_storage(self, request: Request, response: Response):
        """Return file path."""
        storage = request.app.make("storage")
        file_name = request.environ.get('PATH_INFO').split('/')[-1].replace('..', '')
        return response.download(file_name, storage.disk('local').get_path('collapsar/storage/' + file_name))
