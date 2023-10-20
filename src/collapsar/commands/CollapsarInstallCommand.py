# Copy files from assets to storage/public/vendor/collapsar

"""New Resource Command."""
from masonite.commands.Command import Command


class CollapsarInstallCommand(Command):
    """
    Installs collapsar

    collapsar:install
    """

    def __init__(self, application):
        super().__init__()
        self.app = application

    def handle(self):
        pass
