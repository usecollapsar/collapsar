"""BelongsTo Field definition"""
from typing import Union, TYPE_CHECKING
from .Field import Field
from .traits.RelationField import RelationField

if TYPE_CHECKING:
    from masoniteorm.models.Model import Model
    from .Resource import Resource


class BelongsTo(Field, RelationField):
    """BelongsTo Field definition"""

    relation_label: str = ""
    _options = []

    def __init__(
        self,
        name: str,
        attribute: str,
        resource: Union[str, "Resource", None] = None,
    ):
        super().__init__(name, resource)
        # Field's component
        self.component = "BelongsToField"
        # Field's suggestions callback
        self.resource = self.find_resource(resource)
        self.attribute = attribute

    def resolve_value(self, model):
        """Set the display callback"""
        return model[self.attribute].id if model[self.attribute] else None

    def resolve_options(self):
        """Set the display callback"""
        return list(
            map(lambda item: {"label": item.name, "value": item.id}, self.resource.model.all())
        )

    def get_related_local_key(self, model):
        """Get the related local key"""
        return model.get_related(self.attribute).local_key

    def get_related_foreign_key(self, model):
        """Get the related foreign key"""
        return model.get_related(self.attribute).foreign_key

    def get_related_resource(self, model: "Model"):
        """Get the related resource"""
        return self.resource(model[self.attribute])

    def resolve_for_display(self, model):
        """Resolve the field for display"""

        self.value = self.resolve_value(model)

        if model[self.attribute] is not None:
            self.relation_label = self.get_related_resource(model).resolve_label()

        return self

    def fill(self, request, model: "Model"):
        """Fill the field"""
        related_id = request.input(self.attribute)
        setattr(model, self.get_related_local_key(model), related_id)

        return None

    def json_serialize(self):
        """
        Prepare the element for JSON serialization.

        :return: dict
        """
        serialized = super().json_serialize()
        serialized.update({"resource": self.resource.__name__})
        serialized.update({"options": self.resolve_options()})
        serialized.update({"relation_label": self.relation_label})
        serialized.update({"relation_urikey": self.resource.get_urikey()})

        return serialized
