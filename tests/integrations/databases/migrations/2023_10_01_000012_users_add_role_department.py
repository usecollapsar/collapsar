"""UsersAddRoleDepartment Migration."""

from masoniteorm.migrations import Migration


class UsersAddRoleDepartment(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("users") as table:
            table.string("role").nullable()
            table.string("department").nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("users") as table:
            table.drop_column("role", "department")
