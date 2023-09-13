"""A CollapsarProvider Service Provider."""

from masonite.packages import PackageProvider
from masonite.routes import Route
from ..config.filesystem import STATICFILES
from masonite.storage import StorageCapsule

class CollapsarProvider(PackageProvider):

    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("collapsar")
            .name("masonite-collapsar")
            .config("config/collapsar.py", publish=True)
            .controllers('controllers')
            .routes("routes/web.py")
            .views('templates', publish=True)
            .assets('dist')
        )

    def register(self):
        super().register()

        self.staticFiles(STATICFILES)

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