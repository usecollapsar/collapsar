"""A CollapsarController Module."""
from masonite.views import View
from masonite.controllers import Controller
from masonite.response import Response

class CollapsarController(Controller):
    """CollapsarController Controller Class."""

    def index(self, view: View):
        return view.render('masonite-collapsar:admin.index')