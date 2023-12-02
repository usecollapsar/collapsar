from tests.integrations.app.models.User import User
from src.collapsar.Resource import Resource
from src.collapsar.TextInput import TextInput
from src.collapsar.Id import Id
from src.collapsar.Boolean import Boolean
from src.collapsar.Password import Password
from src.collapsar.Calendar import Calendar


class UserResource(Resource):
    """User Resource."""

    index = 10
    label = "name"
    title = "User"
    model = User

    def to_string(self):
        """Return string representation of the resource."""
        return self.model.__name__

    @classmethod
    def fields(cls):
        """Return the fields of the resource."""

        return [
            Id("Id", "id").readonly().sortable(),
            Boolean("Active", "is_active"),
            TextInput("Name", "name").rules("required", "max:40").hide_from_index(),
            TextInput("Email", "email")
            .rules("required", "email", "max:30", "unique:users")
            .sortable(),
            Password("Password", "password")
            .update_rules("nullable", "min:8")
            .hide_from_index(),
            Calendar("Created at", "created_at"),
        ]
