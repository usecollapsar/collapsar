""" Article Model """

from masoniteorm.models import Model
from masoniteorm.scopes import UUIDPrimaryKeyMixin

class Article(Model, UUIDPrimaryKeyMixin):
    """Article Model"""

    __fillable__ = ["title", "content"]
