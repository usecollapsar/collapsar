"""Collapsar class definition"""
from masonite.configuration import config

class Collapsar:
    """Collapsar class definition."""

    application = None
    resources = []

    def __init__(self, application):
        self.application = application
        self.resources = config('collapsar.resources')

    def get_resources(self):
        """Return the resource of given urikey."""
        return self.resources

    def get_resource(self, urikey):
        """Return the resource of given urikey."""

        resource = list(filter(lambda resource: resource.get_urikey() == urikey, self.resources))

        if len(resource) > 0:
            return resource[0]
        else:
            return None