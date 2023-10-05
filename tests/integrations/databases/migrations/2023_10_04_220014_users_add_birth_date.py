"""UsersAddBirthDate Migration."""

from masoniteorm.migrations import Migration


class UsersAddBirthDate(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("users") as table:
            table.date("birth_date").nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("users") as table:
            table.drop_column("birth_date")
