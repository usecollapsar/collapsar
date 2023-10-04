"""UsersAddContent Migration."""

from masoniteorm.migrations import Migration


class UsersAddContent(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("users") as table:
            table.text("content").nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("users") as table:
            table.drop_column("content")
