"""Base class for custom fields"""
import inspect
import sys
from os import path
from .Field import Field


class CustomField(Field):

    custom_field = True
    package_name = None

    def get_script(self):
        module_name = self.__class__.__module__
        module = sys.modules[module_name]
        file_name = inspect.getfile(module)
        return path.join(path.dirname(file_name), "dist/assets/app-bundle.umd.js")

    def json_serialize(self):
        """Returns a dict with the field's data"""

        return {
            **super().json_serialize(),
            "custom_field": True,
            "package_name": self.package_name
        }
