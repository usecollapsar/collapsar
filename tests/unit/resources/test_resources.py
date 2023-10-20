from masonite.tests import TestCase, DatabaseTransactions
from masoniteorm.models import Model
from src.collapsar.Resource import Resource
from src.collapsar.TextInput import TextInput
from src.collapsar.Password import Password
from src.collapsar.Id import Id


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
            Id("Id", "id"),
            TextInput("Name", "name"),
            TextInput("Email", "email"),
            Password("Password", "password"),
            TextInput("Created At", "created_at"),
        ]

    @classmethod
    def index_fields(cls):
        """Return the fields to be displayed in the index page."""
        return ("id", "name", "email", "created_at", "updated_at")


class TestResources(TestCase, DatabaseTransactions):
    """Test Resources Class."""

    connection = "testing"

    def test_resource_can_get_fields(self):
        ur = UserResource
        self.assertEqual(len(ur.fields()), 5)
