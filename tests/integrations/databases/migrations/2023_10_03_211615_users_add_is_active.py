"""UsersAddIsActive Migration."""

from masoniteorm.migrations import Migration


class UsersAddIsActive(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("users") as table:
            table.boolean("is_active").default(False)

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("users") as table:
            table.drop_column("isa_ctive")
