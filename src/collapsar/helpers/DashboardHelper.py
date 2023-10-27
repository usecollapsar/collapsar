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

    def get_user(self):
        """Return the user."""
        user = self.application.make("auth").user()

        if user:
            return {
                "name": user.name,
                "email": user.email,
                "id": user.id,
            }

        return None

    def get_resources_navigation(self):
        """Return the resources navigation."""
        resources = (
            collect(self.get_resources())
            .map(
                lambda resource: {
                    "title": resource.title,
                    "index": resource.index,
                    "group": resource.group,
                    "urikey": resource.get_urikey(),
                }
            )
            .sort("index")
            .group_by("group")
        )

        return resources.all()
