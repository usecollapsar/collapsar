"""A CollapsarProvider Service Provider."""
import json
from masonite.packages import PackageProvider
from masonite.configuration import config

from ..helpers.DashboardHelper import DashboardHelper
from ..foundation.Collapsar import Collapsar
from ..commands.MakeResourceCommand import MakeResourceCommand
from ..commands.CollapsarInstallCommand import CollapsarInstallCommand


class CollapsarProvider(PackageProvider):
    """
    A service provider for the Collapsar package.
    """

    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("collapsar")
            .name("masonite-collapsar")
            .config("config/collapsar.py", publish=True)
            .commands(*self.register_commands())
            .controllers("controllers")
            .routes("routes/web.py", "routes/api.py")
            .views("templates", publish=True)
            .assets("dist")
            .register_helpers()
        )

    def register(self):
        """
        Register the service provider.
        """

        super().register()

        resources_path = config('collapsar.resources_path', 'app/collapsar/resources')

        self.application.bind("Collapsar", Collapsar(self.application))
        self.application.simple(DashboardHelper(self.application))
        self.application.bind("collapsar.resources.location", resources_path)


    def boot(self):
        """Boots services required by the container."""

        # request = self.application.make("request")
        # self.application.bind(
        #     "CollapsarRequest",
        #     CollapsarRequest(request),
        # )

    def register_commands(self):
        return [
            MakeResourceCommand(self.application),
            CollapsarInstallCommand(self.application)
        ]

    def register_helpers(self):
        """Register helpers into the container."""

        def json_encode(data):
            return json.dumps(data)

        self.application.make("view").filter("json_encode", json_encode)
