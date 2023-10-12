""" Article Model """

from masoniteorm.models import Model
from masoniteorm.scopes import UUIDPrimaryKeyMixin
from masoniteorm.relationships import belongs_to
class Article(Model, UUIDPrimaryKeyMixin):
    """Article Model"""

    __fillable__ = ["title", "content", "user_id"]

    @belongs_to('user_id', 'id')
    def user(self):
        from tests.integrations.app.models.User import User
        return User
