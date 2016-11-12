from pyramid.view import view_config, view_defaults


@view_defaults(renderer='json')
class Users:

    def __init__(self, request):
        self.request = request
        self.view_name = 'Users'


    @view_config(route_name='desc')
    def descript_users(self):
        return {'msg': 'Olá'}

    @view_config(route_name='list_users', request_method='GET')
    def list_all_users(self):
        return [{'id': '1', 'username': 'foo'}]

    @view_config(route_name='create_user', request_method='POST')
    def create_user(self):
        return {2: 3}
