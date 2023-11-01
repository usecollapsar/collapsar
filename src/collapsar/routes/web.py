from masonite.routes import Route
from ..controllers.CollapsarController import CollapsarController
from ..controllers.AuthController import AuthController

ROUTES = [
    Route.group(
        [
            Route.get('/', CollapsarController.index).middleware('auth',),
            Route.get("/auth/login", CollapsarController.index).name('login'),
            Route.post("/auth/login", AuthController.login),
            Route.get("/auth/logout", AuthController.logout),

            Route.get("/storage/.*", CollapsarController.get_storage),
            Route.get("/assets/app.js", CollapsarController.get_js),
            Route.get("/assets/style.css", CollapsarController.get_css),


            # Route.get('', CollapsarController.index).middleware('auth',),
            Route.get('.*', CollapsarController.index).middleware('auth',),
        ],
        prefix="/collapsar",
    )
]
