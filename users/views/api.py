from pyramid.view import view_config


@view_config(route_name='user_hello_world', renderer='json')
def user_hello_world(request):
    return {'hello': 'world'}
