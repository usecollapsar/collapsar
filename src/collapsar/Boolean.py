"""Boolean definition"""
from typing import Callable, Union

from masoniteorm.models import Model
from .Field import Field


class Boolean(Field):
    """Boolean definition"""

    type = "boolean"

    def __init__(
        self, name: str, attribute: Union[str, Callable] = None, resolve_callback: Callable = None
    ):
        # Field's component
        self.component = "BooleanField"
        # Field's suggestions callback
        self.suggestions = None

        super().__init__(name, attribute, resolve_callback)


    def fill(self, request, model: Model):
        setattr(
            model,
            self.attribute,
            1 if request.input(self.attribute) == "true" else 0,
        )


    def json_serialize(self):
        """
        Prepare the element for JSON serialization.

        :return: dict
        """
        serialized = super().json_serialize()
        serialized["value"] = bool(self.value)
        return serialized
