"""Base module for all fields"""
from typing import Callable, Any, List, Union, TYPE_CHECKING
from masoniteorm.models import Model
from masonite.container import Container

if TYPE_CHECKING:
    from .Resource import Resource
    from .foundation.Collapsar import Collapsar


class Field:
    """Base class for all fields"""

    # Attributes
    name: str
    attribute: str
    component: str
    resource: "Resource"
    default_value: Any = None
    value: str = ""
    type: str = "string"
    collapsar: "Collapsar"

    _readonly_callback: Callable = None
    _required_callback: Union[bool, Callable] = False
    _computed_callback: Callable = None
    _display_callback: Callable = None
    _resolve_callback: Callable = None
    _show_on_creation_callback: Union[bool, Callable] = True
    _show_on_update_callback: Union[bool, Callable] = True
    _show_on_index_callback: Union[bool, Callable] = True

    _rules: List[str] = []
    _create_rules: List[str] = []
    _update_rules: List[str] = []
    _help_text: str = ""
    _sortable: bool = True
    _nullable: bool = False
    _readonly: bool = False
    _nullable: bool = False

    def __init__(
        self,
        name: str,
        attribute: Union[str, Callable] = None,
        resolve_callback: Callable = None,
        default_value=None,
    ):
        self.name = name
        self.resolve_callback = resolve_callback
        self.collapsar = Container().make("Collapsar")

        self._default_value = default_value

        if callable(attribute):
            self._computed_callback = attribute
            self.attribute = "ComputedField"
        else:
            self.attribute = attribute if attribute is not None else name.lower().replace(" ", "_")

    def display_callback(self, callback: Callable):
        """Set the display callback for the field"""
        self._display_callback = callback
        return self

    def fill(self, request, model: Model):
        """Fill the field"""
        setattr(model, self.attribute, request.input(self.attribute))

        # Added to issues tracker #1: it should return a callback for the field
        return None

    def rules(self, *rules: str):
        """Set the rules for the field"""
        self._rules = rules
        return self

    def create_rules(self, *rules: str):
        """Set of create rules for the field"""
        self._create_rules = rules
        return self

    def update_rules(self, *rules: str):
        """Set of update rules for the field"""
        self._update_rules = rules
        return self

    def required(self, value):
        """Set whether field is required"""
        self._required_callback = value

        return self

    def readonly(self, value: Union[bool, Callable] = True):
        """Set the readonly value or callback the field"""
        self._readonly_callback = value

        return self

    def sortable(self, sortable: bool = True):
        """Set if the field should be sortable or not"""
        self._sortable = sortable
        return self

    def show_on_creation_callback(self, callback: Union[bool, Callable]):
        """Set the show_on_creation callback for the field"""
        self._show_on_creation_callback = callback
        return self

    def hide_from_index(self, callback: Union[bool, Callable] = True):
        """Set the show_on_index callback for the field"""
        self._show_on_index_callback = (
            lambda: not callback() if callable(callback) else not callback
        )
        return self

    def resolve_required(self):
        """Resolve the required value"""
        if (
            self._required_callback is True
            or callable(self._required_callback)
            and self._required_callback()
        ):
            return True

        return False

    def resolve_readonly(self):
        """Resolve the readonly value"""
        if (
            self._readonly_callback is True
            or callable(self._readonly_callback)
            and self._readonly_callback()
        ):
            return True

        return False

    def show_on_index(self):
        """Resolve the show_on_index value"""
        if (
            self._show_on_index_callback is True
            or callable(self._show_on_index_callback)
            and self._show_on_index_callback()
        ):
            return True

        return False

    def show_on_creation(self):
        """Resolve the show_on_creation value"""
        if (
            self._show_on_creation_callback is True
            or callable(self._show_on_creation_callback)
            and self._show_on_creation_callback()
        ):
            return True

        return False

    def resolve_value(self, model: Model):
        """Resolve the field's value"""
        if self.attribute in model.__hidden__:
            return ""

        return getattr(model, self.attribute)

    def resolve_for_display(self, model):
        """Resolve the field for display"""

        if self.attribute == "ComputedField":
            self.value = self._computed_callback(model)
            return self

        if self._display_callback is not None:
            self.value = self._display_callback(model)
            return self

        self.value = self.resolve_value(model)

        return self

    def format_value(self, value):
        """Format the value"""
        return value

    def random_id(self):
        """Generate a random id for the field"""
        import random
        import string

        return "".join(random.choices(string.ascii_lowercase, k=10))

    def json_serialize(self):
        """Returns a dict with the field's data"""
        return {
            "attribute": self.attribute
            if not callable(self._computed_callback)
            else f"computed_{self.random_id()}",
            "help_text": self._help_text,
            "index_name": self.name,
            "name": self.name,
            "field_name": self.__class__.__name__,
            # "nullable": self._nullable,
            # 'panel': self.panel,
            # 'prefixComponent': self.
            "readonly": self.resolve_readonly(),
            "required": self.resolve_required(),
            "sortable": self._sortable,
            "component": self.component,
            "type": self.type,
            # 'sortableUriKey': self.sortableUriKey(),
            # 'textAlign': self.textAlign,
            # 'validationKey': self.validationKey(),
            "computed": callable(self._computed_callback),
            "rules": self._rules,
            "create_rules": self._create_rules,
            "update_rules": self._update_rules,
            "default_value": self._default_value,
            "value": self.format_value(self.value),
        }
