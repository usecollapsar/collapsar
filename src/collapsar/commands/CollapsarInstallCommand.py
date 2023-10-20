# Copy files from assets to storage/public/vendor/collapsar

"""New Resource Command."""
import os
import shutil

from masonite.utils.location import base_path
from masonite.utils.filesystem import make_directory, get_module_dir
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
