from masonite.routes import Route

from ..controllers.ResourceStoreController import ResourceStoreController
from ..controllers.ResourceIndexController import ResourceIndexController
from ..controllers.FieldsController import FieldsController
from ..controllers.ResourceShowController import ResourceShowController
from ..controllers.ResourceUpdateController import ResourceUpdateController
from ..controllers.ResourceDeleteController import ResourceDeleteController


ROUTES = [
    Route.group(
        [
            Route.post("/@resource", ResourceStoreController.handle),
            Route.get("/@resource", ResourceIndexController.handle),
            Route.get("/@resource/creation-fields", FieldsController.creation),
            Route.get("/@resource/@resource_id", ResourceShowController.handle),
            Route.patch("/@resource/@resource_id", ResourceUpdateController.handle),
            Route.delete("/@resource/@resource_id", ResourceDeleteController.handle),
            Route.put("/@resource/", ResourceStoreController.handle),
        ],
        prefix="/collapsar-api",
        middleware=["auth"]
    )
]
