"""Resource Class."""
from masoniteorm.models import Model
# from masoniteorm.scopes import SoftDeletesMixin
# from masonite.authentication import Authenticates
from slugify import slugify

class Resource():
    """Resource Class."""

    title = ""
    model = None
    group = "default"

    def __init__(self, model = None):
        """Resource Constructor."""
        self.model = model if model is not None else self.model

    def to_string(self):
        """Return string representation of the resource."""
        pass

    def fields(self, fields):
        """Return the fields of the resource."""
        return fields
    
    @classmethod
    def json_serialize(self):
        """Prepare the element for JSON serialization."""
        return {
            'title': self.title,
            'fields': list(map(lambda field: field.json_serialize(), self.fields())),
            'index_fields': self.index_fields(),
            'group': self.group,
            'urikey': self.get_urikey()
        }
    
    @classmethod
    def paginate(self, per_page = 10):
        """Paginate the resource."""
        return self.model.paginate(per_page)
    
    @classmethod
    def index_fields(self):
        """Return the fields to be displayed in the index page."""
        return ("id",)
    
    @classmethod
    def get_model(self):
        return getattr(self.model, self.get_title())

    @classmethod
    def get_title(self):
        return self.model.__name__.split('.')[-1]

    @classmethod
    def get_urikey(self):
        """Return the urikey of the resource."""
        # as slug
        return slugify(self.model.__name__.split('.')[-1].lower())