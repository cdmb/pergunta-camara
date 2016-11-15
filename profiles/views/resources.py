from pyramid.security import Allow, Authenticated, Everyone


class ProfilesResource:

    def __init__(self, request):

        self.request = request

    @property
    def __acl__(self):
        return [
            (Allow, Everyone, 'view'),
            (Allow, Authenticated, 'create')
        ]
