from masonite.routes import Route
from ..controllers.CollapsarController import CollapsarController

ROUTES = [
    Route.group([
        Route.get('/', CollapsarController.index)
    ], prefix='/collapsar')
]