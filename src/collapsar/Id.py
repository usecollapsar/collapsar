"""ID Field definition"""
from typing import Callable, Union
from .Field import Field


class Id(Field):
    """ID Field definition"""

    _show_on_creation = False

    def __init__(
        self, name: str, attribute: Union[str, Callable] = None, resolve_callback: Callable = None
    ):
        # Field's component
        self.component = "TextField"
        # Field's suggestions callback
        self.suggestions = None

        super().__init__(name, attribute, resolve_callback)

    def json_serialize(self):
        """
        Prepare the element for JSON serialization.

        :return: dict
        """
        serialized = super().json_serialize()
        serialized['primary_key'] = True
        return serialized
