"""A ResourceStoreController Module."""
from masonite.views import View
from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request

from src.collapsar.helpers.DashboardHelper import DashboardHelper

class ResourceStoreController(Controller):
    """ResourceStoreController Controller Class."""

    def handle(self, request: Request, response: Response, resource):

        resource = request.app.make('Collapsar').get_resource(resource)

        if resource is None:
            return response.json({'success': False})    

        resource_model = resource.get_model().create(request.all())
    
        return response.json({'resource_model': resource_model.json(), 'success': True})