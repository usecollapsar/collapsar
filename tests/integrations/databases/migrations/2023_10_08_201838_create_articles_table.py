"""CreateArticlesTable Migration."""

from masoniteorm.migrations import Migration


class CreateArticlesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("articles") as table:
            table.uuid("id").primary()
            table.string("title")
            table.unsigned_big_integer("user_id")
            table.text("content")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("articles")
