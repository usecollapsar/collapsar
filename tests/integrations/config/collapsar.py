"""Collapsar Settings"""
ROUTE_PREFIX = "/collapsar"
from tests.integrations.app.collapsar.resources.ArticleResource import ArticleResource
from tests.integrations.app.collapsar.resources.UserResource import UserResource

RESOURCES = [
    # Add your resources
    ArticleResource,
    UserResource,
]
