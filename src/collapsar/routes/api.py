from masonite.routes import Route

ROUTES = [
    Route.group([
        Route.post('/@resource', "ResourceStoreController@handle"),
        Route.get('/@resource', "ResourceIndexController@handle"),
        Route.get('/@resource/@resource_id', "ResourceShowController@handle"),
    ], prefix='/collapsar/api')
]