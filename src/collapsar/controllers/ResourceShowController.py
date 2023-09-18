"""A ResourceShowController Module."""
from masonite.views import View
from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request

from src.collapsar.helpers.DashboardHelper import DashboardHelper

class ResourceShowController(Controller):
    """ResourceShowController Controller Class."""

    def handle(self, request: Request, response: Response, resource, resource_id):

        resource = request.app.make('Collapsar').get_resource(resource)

        if resource is None:
            return response.json({'success': False})

        model = resource.model.find(resource_id)

        resource = resource.json_serialize()
    
        return response.json({'data': model.serialize(), 'resource': resource})