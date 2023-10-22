"""ArticleTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from masoniteorm import Factory
from tests.integrations.app.models.Article import Article


class ArticleTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Factory(Article, 50).create()
