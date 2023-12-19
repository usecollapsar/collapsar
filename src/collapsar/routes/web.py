from masonite.routes import Route
from masonite.configuration import config

from ..controllers.CollapsarController import CollapsarController
from ..controllers.ResourceIndexController import ResourceIndexController
from ..controllers.ResourceShowController import ResourceShowController
from ..controllers.ResourceUpdateController import ResourceUpdateController
from ..controllers.AuthController import AuthController

ROUTE_PREFIX = config('collapsar.route_prefix')

ROUTES = [
    Route.get('/collapsar_scripts', CollapsarController.get_script),
    Route.group(
        [
            Route.get("/", CollapsarController.index).middleware(
                "auth",
            ),
            Route.get("/auth/login", AuthController.index).name("login"),
            Route.post("/auth/login", AuthController.login),
            Route.get("/auth/logout", AuthController.logout),
            Route.get("/storage/.*", CollapsarController.get_storage),
            Route.get("/assets/app.js", CollapsarController.get_js),
            Route.get("/assets/style.css", CollapsarController.get_css),
            Route.get("/resource/@resource", ResourceIndexController.index).middleware(
                "auth",
            ),
            Route.get("/resource/@resource/create", ResourceUpdateController.create).middleware(
                "auth",
            ),
            Route.get("/resource/@resource/@resource_id", ResourceShowController.show).middleware(
                "auth",
            ),
            Route.get(
                "/resource/@resource/@resource_id/edit", ResourceUpdateController.edit
            ).middleware(
                "auth",
            ),
            # Route.get('', CollapsarController.index).middleware('auth',),
            # Route.get('.*', CollapsarController.index).middleware('auth',),
        ],
        prefix=ROUTE_PREFIX,
    )
]
