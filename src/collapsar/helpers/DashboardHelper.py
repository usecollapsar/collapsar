"""DashboardHelper module."""
from masonite.utils.collections import collect


class DashboardHelper:
    """DashboardHelper class"""

    resources = []

    def __init__(self, application):
        self.application = application

    def get_resources(self):
        """Return the resources of the given resource."""
        return self.application.make("Collapsar").get_resources()

    def register_resource(self, resource):
        """Register a resource."""
        self.resources.append(resource)

    def get_resources_navigation(self):
        """Return the resources navigation."""
        resources = (
            collect(self.get_resources())
            .map(
                lambda resource: {
                    "title": resource.title,
                    "group": resource.group,
                    "urikey": resource.get_urikey(),
                }
            )
            .group_by("group")
        )

        return resources.all()
