"""A CollapsarProvider Service Provider."""

from masonite.packages import PackageProvider
from masonite.routes import Route
from masonite.storage import StorageCapsule

from ..config.filesystem import STATICFILES
from ..helpers.DashboardHelper import DashboardHelper
from ..foundation import Kernel

import json

class CollapsarProvider(PackageProvider):

    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("collapsar")
            .name("masonite-collapsar")
            .config("config/collapsar.py", publish=True)
            .controllers('controllers')
            .routes("routes/web.py", "routes/api.py")
            .views('templates', publish=True)
            .assets('dist')
            .register_helpers()
        )
        
        self.staticFiles(STATICFILES)

    def register(self):
        super().register()
        
        self.application.bind("Collapsar", Kernel(self.application))
        self.application.simple(DashboardHelper(self.application))

    def boot(self):
        """Boots services required by the container."""
        pass


    def staticFiles(self, files: dict):
        """Add static files to the container."""
        
        storage_capsule = self.application.resolve(StorageCapsule)
        storage_capsule.add_storage_assets(files)

        response_handler = self.application.get_response_handler()

        for location, alias in (
            storage_capsule.get_storage_assets().items()
        ):
            response_handler.add_files(location, prefix=alias)

        self.application.set_response_handler(response_handler)

        return self
    
    def register_helpers(self):
        def json_encode(data):
            return json.dumps(data)
        
        self.application.make('view').filter('json_encode', json_encode)