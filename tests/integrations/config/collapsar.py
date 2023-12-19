"""Collapsar Settings"""
from tests.integrations.app.collapsar.resources.UserResource import UserResource
from tests.integrations.app.collapsar.resources.ArticleResource import ArticleResource
from tests.integrations.app.models.User import User

ROUTE_PREFIX = "/collapsar"

RESOURCES = [
    # define your resources
    UserResource,
    ArticleResource,
]

USER_MODEL = User
