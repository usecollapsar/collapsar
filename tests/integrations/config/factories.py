# config/factories.py
from masoniteorm import Factory
from tests.integrations.app.models.Article import Article


def article_factory(faker):
    return {"title": faker.text(30), "content": faker.text(), "user_id": None}


Factory.register(Article, article_factory)
