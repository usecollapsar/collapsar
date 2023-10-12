"""Collapsar class definition"""
import sys
import os
import importlib
import inspect

from ..config.collapsar import RESOURCES_PATH
from ..Resource import Resource


class Collapsar:
    """Collapsar class definition."""
    application = None
    resources = []

    def __init__(self, application):
        self.application = application
        self.register_resources(RESOURCES_PATH)

    def get_resources(self):
        """Return the resource of given urikey."""
        return list(map(lambda resource: resource["resource"], self.resources))

    def get_resource(self, urikey):
        """Return the resource of given urikey."""

        resource = list(filter(lambda resource: resource["urikey"] == urikey, self.resources))

        if len(resource) > 0:
            return resource[0]["resource"]
        else:
            return None

    def register_resources(self, path):
        """Register resources."""

        subclasses = []

        # Add path to system path for module import

        real_path = self.application.base_path + "/" + path

        sys.path.append(real_path)

        if not os.path.exists(real_path):
            return

        # Iterate over each file in the path
        for filename in os.listdir(real_path):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]  # Removing .py to get the module name

                # Import the module dynamically
                module = importlib.import_module(module_name)

                # Iterate over all objects in the module
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and issubclass(obj, Resource) and obj != Resource:
                        subclasses.append({"urikey": obj.get_urikey(), "resource": obj})

        self.resources = subclasses
