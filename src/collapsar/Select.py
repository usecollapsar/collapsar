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

    def get_display_value(self):
        """Get the display value of the field"""
        if not (len(self._options) > 0 and isinstance(self._options[0], dict)):
            return self.value

        filter_value = list(
            filter(lambda option: str(option["value"]) == self.value, self._options)
        )

        return filter_value[0]["label"] if filter_value else self.value

    def json_serialize(self):
        """
        Prepare the element for JSON serialization.

        :return: dict
        """
        serialized = super().json_serialize()
        serialized.update({"options": self._options})
        serialized.update({"display_value": self.get_display_value()})
        return serialized
