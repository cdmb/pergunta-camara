from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator


def main(global_config, **settings):

    """ This function returns a Pyramid WSGI application. """

    config = Configurator(settings=settings)

    config.include('users', route_prefix='/api')

    config.set_authorization_policy(ACLAuthorizationPolicy())
    # Enable JWT authentication.
    config.include('pyramid_jwt')
    config.set_jwt_authentication_policy('secret')

    config.scan()
    return config.make_wsgi_app()
