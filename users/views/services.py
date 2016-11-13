from pyramid.view import view_config, view_defaults


@view_defaults(renderer='json')
class Users:

    def __init__(self, request):
        self.request = request
        self.view_name = 'Users'

    @view_config(route_name='create_users', request_method='GET')
    def create(self):
        return {'result': 'ok'}
