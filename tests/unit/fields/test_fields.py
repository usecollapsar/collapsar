from masonite.tests import TestCase
from masoniteorm.models import Model
from src.collapsar.Resource import Resource
from src.collapsar.TextField import TextField
from src.collapsar.PasswordField import PasswordField
from src.collapsar.IdField import IdField


class User(Model):
    """User Model"""

    __fillable__ = ["name", "email", "password"]
    __auth__ = "email"

    @property
    def meta(self):
        return 1


class UserResource(Resource):
    """User Resource."""

    title = "User"
    model = User

    def to_string(self):
        """Return string representation of the resource."""
        return self.model.__name__

    @classmethod
    def fields(cls):
        """Return the fields of the resource."""

        return [
            IdField("Id", "id"),
            TextField("Name", "name"),
            TextField("Email", "email"),
            PasswordField("Password", "password"),
            TextField("Created At", "created_at"),
        ]

    @classmethod
    def index_fields(cls):
        """Return the fields to be displayed in the index page."""
        return ("id", "name", "email", "created_at", "updated_at")


class TestFields(TestCase):
    """Test Resources Class."""

    def test_field_properties(self):
        field = TextField("Name", "name")
        
        field.readonly(True)
        self.assertTrue(field.resolve_readonly())

        field.readonly(False)
        self.assertFalse(field.resolve_readonly())

        def false_callback():
            return False

        field.readonly(false_callback)
        self.assertTrue(callable(field._readonly_callback))
        self.assertFalse(field.resolve_readonly())

    def test_field_rules(self):
        field = TextField("Name", "name")
        field.rules("required", "max:255")
        self.assertEqual(field._rules, ("required", "max:255"))