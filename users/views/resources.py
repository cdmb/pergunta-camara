from pyramid.security import Allow, Authenticated, Everyone


class UsersResource:

    def __init__(self, request):
        self.request = request

    @property
    def __acl__(self):
        return [
            (Allow, Everyone, 'create'),
            (Allow, Authenticated, 'view')
        ]
