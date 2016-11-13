def includeme(config):

    # Users service
    config.add_route('create_users', '/users/create')

    # Auth service
    config.add_route('login', '/login')
