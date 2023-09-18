from src.collapsar import Resource
from tests.integrations.app.models.User import User
from src.collapsar.TextField import TextField

class UserResource(Resource):
    """User Resource."""

    title = "User"
    model = User

    @classmethod
    def to_string(self):
        """Return string representation of the resource."""
        return self.model.__name__
    
    @classmethod
    def fields(self):
        """Return the fields of the resource."""

        return [
            TextField('name', 'Name', 'text'),
            TextField('email', 'Email', 'text'),
        ]

    @classmethod
    def index_fields(self):
        """Return the fields to be displayed in the index page."""
        return ("id", "name", "email", "created_at", "updated_at")