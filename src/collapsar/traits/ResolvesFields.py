"""A trait that provides a method to resolve a list of fields to their values."""
from abc import ABCMeta, abstractmethod
from masoniteorm.models import Model

class ResolvesFields(metaclass=ABCMeta):
    """A trait that provides a method to resolve a list of fields to their values."""

    @classmethod
    def fields(cls):
        """Return the fields of the resource."""

    @classmethod
    @abstractmethod
    def get_model(cls) -> Model:
        """Return the model of the resource."""

    @classmethod
    def creation_fields(cls):
        """Resolve a list of fields to their values."""
        resolved_fields = []
        for field in cls._filter_only_fillable(cls.fields()):
            if field.show_on_creation:
                resolved_fields.append(field)
        return resolved_fields
    
    @classmethod
    def creation_fields_without_readonly(cls):
        """Resolve a list of fields to their values."""
        resolved_fields = []
        for field in cls.creation_fields():
            if not field.is_readonly():
                resolved_fields.append(field)
        return resolved_fields

    @classmethod
    def show_fields(cls):
        """Resolve a list of fields to their values."""
        resolved_fields = []
        for field in cls.fields():
            if field.show_on_index:
                resolved_fields.append(field)
        return resolved_fields

    @classmethod
    def _filter_only_fillable(cls, fields):
        """Remove hidden fields from the resource."""
        model = cls.get_model()

        return [field for field in fields if field.attribute in model.__fillable__]
