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
        {--f|force=? : Force overriding file if already exists}
    """

    def __init__(self, application):
        super().__init__()
        self.app = application

    def handle(self):
        filepath = base_path("storage/public/vendor/collapsar")
        make_directory(filepath)
        if os.path.exists(filepath) and not self.option("force"):
            self.warning(
                f"{filepath} already exists! Run the command with -f (force) to override."
            )
            return -1

        assets_path = os.path.join(get_module_dir(__file__), "../dist")
        for file in os.listdir(os.path.join(get_module_dir(__file__), "../dist")):
            source = os.path.join(assets_path, file)
            dest = os.path.join(filepath, file)

            if os.path.exists(dest) and not self.option("force"):
                self.warning(
                    f"{dest} already exists! Run the command with -f (force) to override."
                )
                return -1

            result = shutil.copytree(source, dest, dirs_exist_ok=True)

            self.info(f"File Created ({result})")
