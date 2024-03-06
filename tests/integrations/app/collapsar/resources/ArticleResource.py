from tests.integrations.app.models.Article import Article

from src.collapsar import Resource
from src.collapsar.TextInput import TextInput
from src.collapsar.Id import Id
from src.collapsar.RichText import RichText
from src.collapsar.BelongsTo import BelongsTo
from src.collapsar.Image import Image
from src.collapsar.Markdown import Markdown

class ArticleResource(Resource):
    """Article Resource."""

    label = "Article"
    title = "Articles"
    model = Article
    search_fields = ["title", "id"]

    def to_string(self):
        """Return string representation of the resource."""
        return self.model.__name__

    @classmethod
    def query(cls):
        """Return the query of the resource."""
        return cls.model().query().where_not_null("user_id")

    @classmethod
    def fields(cls):
        """Return the fields of the resource."""

        return [
            Id("Id", "id").readonly(),
            Image("Image", "image"),
            TextInput("Title", "title").rules("required"),
            Markdown("Content", "content").rules("required").hide_from_index(),
            BelongsTo("User", "user", "UserResource").rules("required"),
        ]