from pyramid.view import view_config, view_defaults


@view_defaults(route_name='users', renderer='json')
class Users:

    def __init__(self, request):
        self.request = request

    @view_config(request_method='POST')
    def post(self):
        return {'result': 'ok'}

    @view_config(request_method='GET', permission='view')
    def get(self):
        return {'result': 'ok'}
