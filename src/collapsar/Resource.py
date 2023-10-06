"""Resource Class."""
from slugify import slugify
from masoniteorm.models import Model
from masonite.utils.collections import Collection
from .traits.ResolvesFields import ResolvesFields
from .traits.ForwardsCalls import ForwardsCalls
from .traits.FillsFields import FillsFields
from .CollapsarRequest import CollapsarRequest

class Resource(ResolvesFields, ForwardsCalls, FillsFields):
    """Resource Class."""

    title = ""
    model: "Model"
    group = "default"
    resource: "Model"

    def __init__(self, resource=None):
        """Resource Constructor."""
        self.resource = resource

    def to_string(self):
        """Return string representation of the resource."""

    @classmethod
    def fields(cls):
        """Return the fields of the resource."""

    @classmethod
    def paginate(cls, collapsar_request: "CollapsarRequest"):
        """Paginate the resource."""
        paginator = cls.model.paginate(collapsar_request.param("per_page", 10))

        def _resolve_fields(model, resource):
            return (
                Collection(resource.index_fields())
                .map(lambda field: field.resolve_for_display(model))
                .map(lambda field: field.json_serialize())
                .all()
            )
        
        data = (
            Collection(paginator.result)
            .map(lambda model: _resolve_fields(model, cls))
            .map(cls.fields_to_object)
            .all()
        )

        paginator = paginator.serialize()
        paginator["data"] = data
        paginator["fields"] = list(data[0].keys()) if len(data) > 0 else []
        
        return paginator
    
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
