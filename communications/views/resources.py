from pyramid.security import Allow, Authenticated


class MessagesResource:

    def __init__(self, request):
        self.request = request

    @property
    def __acl__(self):
        return [
            (Allow, Authenticated, 'view')
            (Allow, Authenticated, 'created')
        ]
