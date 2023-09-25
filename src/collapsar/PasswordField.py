"""PasswordField Field definition"""
from typing import Callable, Union, TYPE_CHECKING
from masonite.facades.Hash import Hash
from .Field import Field

if TYPE_CHECKING:
    from masoniteorm.models.Model import Model


class PasswordField(Field):
    """PasswordField Field definition"""

    def __init__(
        self, name: str, attribute: Union[str, Callable] = None, resolve_callback: Callable = None
    ):
        # Field's component
        self.component = "PasswordField"
        # Field's suggestions callback
        self.suggestions = None

        super().__init__(name, attribute, resolve_callback)

    def fill(self, request, model: "Model"):
        """Fill the field"""
        setattr(model, self.attribute, Hash.make(request.input(self.attribute)))

        return None

    def json_serialize(self):
        """
        Prepare the element for JSON serialization.

        :return: dict
        """
        serialized = super().json_serialize()
        return serialized
