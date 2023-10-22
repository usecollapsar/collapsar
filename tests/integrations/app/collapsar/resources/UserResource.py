from tests.integrations.app.models.User import User
from src.collapsar import Resource
from src.collapsar.TextInput import TextInput
from src.collapsar.Id import Id
from src.collapsar.Select import Select
from src.collapsar.Boolean import Boolean
from src.collapsar.Password import Password
from src.collapsar.Calendar import Calendar
from src.collapsar.RichText import RichText


class UserResource(Resource):
    """User Resource."""

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
            TextInput("Name + ID (computed)", lambda user: f"(#{user.id}) {user.name} "),
            RichText("Content", "content").hide_from_index(),
            Select("Role", "role").options(["admin", "user"]).rules("required").sortable(),
            Select("Department", "department")
            .options(
                [
                    {"label": "IT", "value": 1},
                    {"label": "Marketing", "value": 2},
                    {"label": "Sales", "value": 3},
                ]
            )
            .rules("required")
            .sortable(),
            Password("Password", "password")
            .update_rules("nullable", "min:8")
            .hide_from_index(),
            Calendar("Birth Date", "birth_date").hide_from_index(),
            TextInput(
                "Created At (computed)", lambda user: user.created_at.strftime("%d/%m/%Y %H:%M:%S")
            ).hide_from_index(),
        ]
