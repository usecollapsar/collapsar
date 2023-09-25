"""Resource Class."""
from slugify import slugify
from masoniteorm.models import Model
from .traits.ResolvesFields import ResolvesFields
from .traits.ForwardsCalls import ForwardsCalls
from .traits.FillsFields import FillsFields


class Resource(ResolvesFields, ForwardsCalls, FillsFields):
    """Resource Class."""

    title = ""
    model: Model
    group = "default"
    resource: Model

    def __init__(self, resource=None):
        """Resource Constructor."""
        self.resource = resource

    def to_string(self):
        """Return string representation of the resource."""

    @classmethod
    def fields(cls):
        """Return the fields of the resource."""

    @classmethod
    def paginate(cls, per_page=10):
        """Paginate the resource."""
        return cls.model.paginate(per_page)

    @classmethod
    def index_fields(cls):
        """Return the fields to be displayed in the index page."""
        return ("id",)

    @classmethod
    def get_model(cls) -> Model:
        """Return the model of the resource."""
        return cls.model

    @classmethod
    def get_title(cls):
        """Return the title of the resource."""
        return cls.model.__name__.split(".")[-1]

    @classmethod
    def get_urikey(cls):
        """Return the urikey of the resource."""
        # as slug
        return slugify(cls.model.__name__.split(".")[-1].lower())

    @classmethod
    def json_serialize(cls):
        """Prepare the element for JSON serialization."""
        return {
            "title": cls.title,
            "index_fields": cls.index_fields(),
            "group": cls.group,
            "urikey": cls.get_urikey(),
        }

    @classmethod
    def new_model(cls):
        """Return a new model instance."""
        return cls.model()

    def __getattr__(self, name):
        if hasattr(self.resource, name):
            return getattr(self.resource, name)

        return self.forwards_call_to(self.resource, name)
