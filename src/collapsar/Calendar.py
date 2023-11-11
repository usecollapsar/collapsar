"""Calendar field class."""
import re
from typing import Callable, Union, TYPE_CHECKING
from datetime import datetime
from .Field import Field

if TYPE_CHECKING:
    from masoniteorm.models.Model import Model


class Calendar(Field):
    """
    Calendar field class.

    Attributes:
        type (str): The type of the calendar field.
        component (str): The component of the field.
        suggestions (callable): The suggestions callback of the field.
    """

    type = "date"
    component = "CalendarField"
    suggestions = None

    def __init__(
        self, name: str, attribute: Union[str, Callable] = None, resolve_callback: Callable = None
    ):
        """
        Initializes a new instance of the Calendar class.

        Args:
            name (str): The name of the field.
            attribute (Union[str, Callable], optional): The attribute of the field. Defaults to None.
            resolve_callback (Callable, optional): The resolve callback of the field. Defaults to None.
        """
        super().__init__(name, attribute, resolve_callback)

    def fill(self, request, model: "Model"):
        """
        Fill the field.

        Args:
            request: The request object.
            model (Model): The model object.
        """

        date_string_without_timezone = re.sub(
            r"GMT[+-]\d{4}\s\(.*\)", "", request.input(self.attribute)
        ).strip()
        date_format = "%a %b %d %Y %H:%M:%S"
        setattr(
            model,
            self.attribute,
            datetime.strptime(date_string_without_timezone, date_format),
        )

    def get_date_format(self):
        """
        Returns the date format based on the type of the calendar.

        If the calendar type is 'datetime', the format will be '%Y-%m-%dT%H:%M:%S.%fZ'.
        If the calendar type is not 'datetime', the format will be '%Y-%m-%d'.

        Returns:
            str: The date format string.
        """
        return "%Y-%m-%d %H:%M:%S" if self.type == "datetime" else "%Y-%m-%d"

    def datetime(self):
        """
        Sets the type of the calendar field to 'datetime'.
        """
        self.type = "datetime"

    def date(self):
        """
        Sets the type of the calendar field to 'date'.
        """
        self.type = "date"

    def format_value(self, value: "datetime"):
        """
        Format the value for display.

        Args:
            value (datetime): The value to format.

        Returns:
            str: The formatted value.
        """
        return value.strftime(self.get_date_format()) if value else None

    def json_serialize(self):
        """
        Prepare the element for JSON serialization.

        Returns:
            dict: The serialized element.
        """
        serialized = super().json_serialize()
        return serialized
