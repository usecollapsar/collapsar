from masonite.routes import Route
from ..controllers.CollapsarController import CollapsarController

ROUTES = [
    Route.group(
        [
            Route.get("/", CollapsarController.index),
            Route.get("/resource/@urikey", CollapsarController.index),
            Route.get("/resource/@urikey/@id", CollapsarController.index),
            Route.get("/resource/@urikey/@id/edit", CollapsarController.index),
        ],
        prefix="/collapsar",
    )
]
