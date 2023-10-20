from masonite.routes import Route
from ..controllers.CollapsarController import CollapsarController

ROUTES = [
    Route.group(
        [
            Route.get("/assets/app.js", CollapsarController.get_js),
            Route.get("/assets/style.css", CollapsarController.get_css),

            Route.get("/", CollapsarController.index),
            Route.get("/resource/@urikey", CollapsarController.index),
            Route.get("/resource/@urikey/@id", CollapsarController.index),
            Route.get("/resource/@urikey/@id/edit", CollapsarController.index),
        ],
        prefix="/collapsar",
    )
]
