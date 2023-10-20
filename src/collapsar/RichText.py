"""RichTextField field class."""
from typing import Callable, Union
from .Field import Field


class RichText(Field):
    """RichTextField field class."""

    def __init__(
        self, name: str, attribute: Union[str, Callable] = None, resolve_callback: Callable = None
    ):
        # Field's component
        self.component = "RichTextField"
        # Field's suggestions callback
        self.suggestions = None

        super().__init__(name, attribute, resolve_callback)

    def json_serialize(self):
        """
        Prepare the element for JSON serialization.

        :return: dict
        """
        serialized = super().json_serialize()
        serialized["value"] = str(self.value)
        return serialized
