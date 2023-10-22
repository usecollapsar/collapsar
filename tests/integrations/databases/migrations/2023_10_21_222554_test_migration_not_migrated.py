"""TestMigrationNotMigrated Migration."""

from masoniteorm.migrations import Migration


class TestMigrationNotMigrated(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("test_migration_not_migrateds") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("test_migration_not_migrateds")
