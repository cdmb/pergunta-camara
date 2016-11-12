from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.authentication import AuthTktAuthenticationPolicy


def includeme(config):

    # Defining base authentication and authorization objects
    authentication_policy = AuthTktAuthenticationPolicy(
        secret=config.settings['pergunta_camara.secret'],
        timeout=config.settings['auth.timeout'],
        reissue_time=config.settings['auth.reissue_time'],
        max_age=config.settings['auth.max_age']
    )
    authorization_policy = ACLAuthorizationPolicy()

    # Set app auth/authorization policies
    config.authorization_policy = authorization_policy
    config.authentication_policy = authentication_policy

    # Pyramid-jwt config
    config.set_authorization_policy(authentication_policy)
    config.include('pyramid_jwt')
    config.set_jwt_authentication_policy('secret')
