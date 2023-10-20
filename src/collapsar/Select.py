"""SelectField Field definition"""
from typing import Callable, Union, TYPE_CHECKING
from .Field import Field

if TYPE_CHECKING:
    from masoniteorm.models.Model import Model


class Select(Field):
    """SelectField Field definition"""

    _options: list = []

    def __init__(
        self, name: str, attribute: Union[str, Callable] = None, resolve_callback: Callable = None
    ):
        # Field's component
        self.component = "SelectField"
        # Field's suggestions callback
        self.suggestions = None

        super().__init__(name, attribute, resolve_callback)

    def options(self, options: list):
        """Set the options for the select field"""
        self._options = options
        return self

    def json_serialize(self):
        """
        Prepare the element for JSON serialization.

        :return: dict
        """
        serialized = super().json_serialize()
        serialized.update({"options": self._options})
        return serialized
