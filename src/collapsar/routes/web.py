from masonite.routes import Route

ROUTES = [
    Route.group([
        Route.get('/', "CollapsarController@index"),
        Route.get("/resource/@urikey", "CollapsarController@index"),
        Route.get("/resource/@urikey/@id", "CollapsarController@index"),
    ], prefix='/collapsar')
]