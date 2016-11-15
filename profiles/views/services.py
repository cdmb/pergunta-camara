from pyramid.view import view_config, view_defaults


@view_defaults(route_name='profiles', renderer='json')
class Profiles:

    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET', permission='view')
    def get(self):
        return {'profiles': []}

    @view_config(request_method='POST', permission='create')
    def post(self):
        return {'created': 'ok'}
