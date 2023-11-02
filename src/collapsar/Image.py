"""ImageField definition"""
from typing import Callable, Union, TYPE_CHECKING
from masonite.facades.Hash import Hash
from .Field import Field

if TYPE_CHECKING:
    from masoniteorm.models.Model import Model


class Image(Field):
    """ImageField definition"""

    type = "file"

    def __init__(
        self, name: str, attribute: Union[str, Callable] = None, resolve_callback: Callable = None
    ):
        # Field's component
        self.component = "ImageField"
        # Field's suggestions callback
        self.suggestions = None

        super().__init__(name, attribute, resolve_callback)

    def fill(self, request, model: "Model"):
        """Fill the field"""

        if isinstance(request.input(self.attribute), str):
            # front send the path of the file when it's already uploaded
            return

        storage = request.app.make("storage")
        path = storage.disk("local").put_file("collapsar/storage/", request.input(self.attribute))
        setattr(model, self.attribute, path)

        return None

    # def update_rules(self, *rules: str):
    #     return rules or ("nullable",)

    def json_serialize(self):
        """
        Prepare the element for JSON serialization.

        :return: dict
        """
        serialized = super().json_serialize()
        return serialized
