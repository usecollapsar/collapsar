from tests.integrations.app.models.User import User
from src.collapsar import Resource
from src.collapsar.TextField import TextField
from src.collapsar.IdField import IdField
from src.collapsar.SelectField import SelectField
from src.collapsar.PasswordField import PasswordField


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
            IdField("Id", "id").readonly().sortable(),

            TextField("Name", "name").rules("required", "max:40").sortable(),

            TextField("Email", "email").rules("required", "email", "max:30", "unique:users").sortable(),

            TextField("Name + ID (computed)", lambda user: f"(#{user.id}) {user.name} "),

            SelectField("Role", "role").options(["admin", "user"]).rules("required").sortable(),

            SelectField("Department", "department")
            .options(
                [
                    {"label": "IT", "value": 1},
                    {"label": "Marketing", "value": 2},
                    {"label": "Sales", "value": 3},
                ]
            )
            .rules("required")
            .sortable(),

            PasswordField("Password", "password").update_rules("nullable", "min:8"),

            TextField("Created At (computed)", lambda user: user.created_at.strftime("%d/%m/%Y %H:%M:%S")),
        ]

    @classmethod
    def index_fields(cls):
        """Return the fields to be displayed in the index page."""
        return ("id", "name", "email", "created_at", "updated_at")
