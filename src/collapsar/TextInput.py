"""TextInput field class."""
from typing import Callable, Union, List
from .Field import Field


class TextInput(Field):
    """TextInput field class."""

    def __init__(
        self, name: str, attribute: Union[str, Callable] = None, resolve_callback: Callable = None
    ):
        # Field's component
        self.component = "TextField"
        # Field's suggestions callback
        self.suggestions = None

        super().__init__(name, attribute, resolve_callback)

    def set_suggestions(self, suggestions: Union[List, Callable]):
        """
        Set the callback or list to be used to determine the field's suggestions list.

        :param suggestions: List or callback for suggestions
        :return: self
        """
        self.suggestions = suggestions
        return self

    def resolve_suggestions(self, request):
        """
        Resolve the display suggestions for the field.

        :param request: NovaRequest instance
        :return: List or None
        """
        if callable(self.suggestions):
            return self.suggestions(request) or None
        return self.suggestions

    def json_serialize(self):
        """
        Prepare the element for JSON serialization.

        :return: dict
        """
        serialized = super().json_serialize()
        serialized["value"] = str(self.value)
        return serialized
