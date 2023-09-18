"""A ResourceIndexController Module."""
from masonite.views import View
from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request

from src.collapsar.helpers.DashboardHelper import DashboardHelper

class ResourceIndexController(Controller):
    """ResourceIndexController Controller Class."""

    def handle(self, request: Request, response: Response, resource):

        resource = request.app.make('Collapsar').get_resource(resource)

        if resource is None:
            return response.json({'success': False})

        paginator = resource.paginate(per_page=10)
    
        return response.json({
            'paginator': paginator.serialize(),
            'fields': resource.index_fields(),               
        })