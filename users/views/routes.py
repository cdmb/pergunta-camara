def includeme(config):
    config.add_route('desc', '/users')
    config.add_route('list_users', '/users/list')
    config.add_route('create_user', '/users/create')
