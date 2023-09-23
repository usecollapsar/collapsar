from masonite.routes import Route

ROUTES = [
    Route.group([
        Route.post('/@resource', "ResourceStoreController@handle"),
        Route.get('/@resource', "ResourceIndexController@handle"),
        Route.get('/@resource/creation-fields', "FieldsController@creation"),
        Route.get('/@resource/@resource_id', "ResourceShowController@handle"),
        Route.patch('/@resource/@resource_id', "ResourceUpdateController@handle"),
        Route.put('/@resource/', "ResourceStoreController@handle"),
    ], prefix='/collapsar/api')
]