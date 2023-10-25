"""A trait to identify relation fields."""
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..foundation.Collapsar import Collapsar
    from ..Resource import Resource


class RelationField:
    """A trait to identify relation fields."""

    collapsar: "Collapsar"

    def find_resource(self, resource_name: Union[str, "Resource"]):
        """Find a resource by name"""
        if not isinstance(resource_name, str):
            return resource_name

        for resource in self.collapsar.get_resources():
            if resource.__name__ == resource_name:
                return resource

        raise ValueError(f"Resource {resource_name} not found")
