"""User Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masonite.authentication import Authenticates

class User(Model, SoftDeletesMixin, Authenticates):
    """User Model."""

    __dates__ = ["created_at"]

    __fillable__ = [
        "name",
        "email",
        "password",
        "role",
        "is_active",
        "department",
        "content",
        "created_at",
    ]
    __hidden__ = ["password"]
    __auth__ = "email"
