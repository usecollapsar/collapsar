"""Calendar field class."""
from typing import Callable, Union, TYPE_CHECKING
from datetime import datetime
from .Field import Field

if TYPE_CHECKING:
    from masoniteorm.models.Model import Model


class Calendar(Field):
    """Calendar field class."""

    type = "date"

    def __init__(
        self, name: str, attribute: Union[str, Callable] = None, resolve_callback: Callable = None
    ):
        # Field's component
        self.component = "CalendarField"
        # Field's suggestions callback
        self.suggestions = None

        super().__init__(name, attribute, resolve_callback)

    def fill(self, request, model: "Model"):
        """Fill the field"""
        setattr(
            model,
            self.attribute,
            datetime.strptime(request.input(self.attribute), "%Y-%m-%dT%H:%M:%S.%fZ"),
        )

    def format_value(self, value: "datetime"):
        """Format the value for display."""
        return value.strftime("%Y-%m-%d") if value else None

    def json_serialize(self):
        """
        Prepare the element for JSON serialization.

        :return: dict
        """
        serialized = super().json_serialize()
        return serialized
