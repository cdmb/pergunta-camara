from .resources import UsersResource


def includeme(config):

    # Users service
    config.add_route('users', '/users', factory=UsersResource)

    # Auth service
    config.add_route('login', '/login')
