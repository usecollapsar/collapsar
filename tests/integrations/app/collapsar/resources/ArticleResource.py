from tests.integrations.app.models.Article import Article
from src.collapsar import Resource
from src.collapsar.TextField import TextField
from src.collapsar.IdField import IdField
from src.collapsar.SelectField import SelectField
from src.collapsar.BooleanField import BooleanField
from src.collapsar.PasswordField import PasswordField
from src.collapsar.CalendarField import CalendarField
from src.collapsar.RichTextField import RichTextField


class ArticleResource(Resource):
    """Article Resource."""

    title = "Article"
    model = Article

    def to_string(self):
        """Return string representation of the resource."""
        return self.model.__name__

    @classmethod
    def fields(cls):
        """Return the fields of the resource."""

        return [
            IdField("Id", "id").readonly(),
            TextField("Title", "title").rules("required"),
            RichTextField("Content", "content").rules("required").hide_from_index(),
        ]
