from pyramid.authorization import ACLAuthorizationPolicy


def includeme(config):

    authorization_policy = ACLAuthorizationPolicy()

    # Set app auth/authorization policies
    # config.set_authentication_policy(authentication_policy)
    config.set_authorization_policy(authorization_policy)

    # Pyramid-jwt config
    config.include('pyramid_jwt')
    config.set_jwt_authentication_policy(
        config.registry.settings['pergunta_camara.secret']
    )
