from pyramid.view import view_config, view_defaults

from pergunta_camara.utils.auth import authenticate_user


@view_defaults(renderer='json')
class Auth:

    def __init__(self, request):

        self.request = request
        self.view_name = 'Auth'

    @view_config(route_name='login', request_method='POST')
    def login(self):

        login = self.request.json_body['login']
        password = self.request.json_body['password']

        user = authenticate_user(login, password)

        if not user:
            return {'result': 'error'}

        return {
            'result': 'ok',
            'token': self.request.create_jwt_token(user.id)
        }
