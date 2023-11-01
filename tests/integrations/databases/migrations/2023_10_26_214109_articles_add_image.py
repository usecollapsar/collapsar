"""ArticlesAddImage Migration."""

from masoniteorm.migrations import Migration


class ArticlesAddImage(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("articles") as table:
            table.string("image").nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("articles") as table:
            table.drop_column("image")
