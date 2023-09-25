"""Base module for all fields"""
from typing import Callable, Any, List, Union, TYPE_CHECKING
from masoniteorm.models import Model

if TYPE_CHECKING:
    from src.collapsar.Resource import Resource


class Field:
    """Base class for all fields"""
    # Attributes
    name: str
    attribute: str
    component: str
    default_value: Any = None
    sortable: bool = True
    nullable: bool = False
    null_values: List[str]
    help_text: str = ""
    resource: "Resource"
    nullable: bool = False
    rules: List[str]
    creation_rules: List[str]
    update_rules: List[str]
    show_on_creation: bool = True
    show_on_update: bool = True
    show_on_index: bool = True
    computed_callback: Callable
    display_callback: Callable
    resolve_callback: Callable

    # pivot: bool
    # fillCallback: Callable
    # customComponents: List[Any]
    # defaultCallback: Callable
    # readonlyCallback: Callable
    # requiredCallback: Callable

    def __init__(
        self, name: str, attribute: Union[str, Callable] = None, resolve_callback: Callable = None
    ):
        self.name = name
        self.resolve_callback = resolve_callback

        self.default(None)

        if callable(attribute):
            self.computed_callback = attribute
            self.attribute = "ComputedField"
        else:
            self.attribute = attribute if attribute is not None else name.lower().replace(" ", "_")

    def default(self, value: Any):
        """Set the default value for the field"""
        self.default_value = value
        return self

    def set_sortable(self, sortable: bool = True):
        """Set if the field should be sortable or not"""
        self.sortable = sortable
        return self

    def set_display_callback(self, callback: Callable):
        """Set the display callback for the field"""
        self.display_callback = callback
        return self

    def is_readonly(self):
        """Set whether field is readonly"""
        return False

    def is_required(self):
        """Set whether field is required"""
        return False

    def get_value(self):
        """Returns field value"""
        return self.default_value

    def fill(self, request, model: Model):
        """Fill the field"""
        setattr(model, self.attribute, request.input(self.attribute))

        # Added to issues tracker #1: it should return a callback for the field
        return None

    def json_serialize(self):
        """Returns a dict with the field's data"""
        return {
            "attribute": self.attribute,
            "help_text": self.help_text,
            "index_name": self.name,
            "name": self.name,
            "nullable": self.nullable,
            # 'panel': self.panel,
            # 'prefixComponent': self.
            "readonly": self.is_readonly(),
            "required": self.is_required(),
            "sortable": self.sortable,
            "component": self.component,
            # 'sortableUriKey': self.sortableUriKey(),
            # 'textAlign': self.textAlign,
            # 'validationKey': self.validationKey(),
            "rules": [],
            "value": self.get_value(),
        }
