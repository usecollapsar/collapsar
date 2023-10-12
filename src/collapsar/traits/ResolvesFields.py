"""A trait that provides a method to resolve a list of fields to their values."""
from abc import abstractmethod
from typing import List, TYPE_CHECKING
from masoniteorm.models import Model
from .RelationField import RelationField
from ..BelongsTo import BelongsTo

if TYPE_CHECKING:
    from src.collapsar.Field import Field
    from src.collapsar.CollapsarRequest import CollapsarRequest


class ResolvesFields:
    """A trait that provides a method to resolve a list of fields to their values."""

    @classmethod
    def fields(cls) -> List["Field"]:
        """Return the fields of the resource."""

    @classmethod
    @abstractmethod
    def get_model(cls) -> Model:
        """Return the model of the resource."""

    @classmethod
    def creation_fields(cls):
        """Resolve a list of fields to their values."""
        return [
            field for field in cls._filter_only_fillable(cls.fields()) if field.show_on_creation()
        ]

    @classmethod
    def creation_fields_without_readonly(cls):
        """Resolve a list of fields to their values."""
        return [field for field in cls.creation_fields() if not field.resolve_readonly()]

    @classmethod
    def show_fields(cls, request: "CollapsarRequest"):
        """Resolve a list of fields to their values."""
        fields = [field for field in cls.fields() if field.show_on_creation()]

        return map(lambda field: field.resolve_for_display(request.model()), fields)

    @classmethod
    def index_fields(cls):
        """Return the fields to be displayed in the index page."""
        return [field for field in cls.fields() if field.show_on_index()]

    @classmethod
    def fields_to_object(cls, fields: List["Field"]):
        """Reduce a list of fields to their values."""
        obj = {}
        for field in fields:
            obj.update(
                {
                    field["attribute"]: field["relation_label"]
                    if "relation_label" in field.keys()
                    else field["value"]
                }
            )
        return obj

    @classmethod
    def _filter_only_fillable(cls, fields) -> List["Field"]:
        """Remove hidden fields from the resource."""
        model = cls.get_model()
        return [
            field
            for field in fields
            if isinstance(field, RelationField) or field.attribute in model.__fillable__
        ]
