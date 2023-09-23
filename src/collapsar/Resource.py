"""Resource Class."""
from slugify import slugify
from masoniteorm.models import Model
from collapsar.traits.ResolvesFields import ResolvesFields


class Resource(ResolvesFields):
    """Resource Class."""

    title = ""
    model = None
    group = "default"

    def __init__(self, model=None):
        """Resource Constructor."""
        self.model = model if model is not None else self.model

    def to_string(self):
        """Return string representation of the resource."""

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
        return cls.model.__name__.split('.')[-1]

    @classmethod
    def get_urikey(cls):
        """Return the urikey of the resource."""
        # as slug
        return slugify(cls.model.__name__.split('.')[-1].lower())
    

    @classmethod
    def json_serialize(cls):
        """Prepare the element for JSON serialization."""
        return {
            'title': cls.title,
            'index_fields': cls.index_fields(),
            'group': cls.group,
            'urikey': cls.get_urikey()
        }