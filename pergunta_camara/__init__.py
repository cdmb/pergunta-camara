from pyramid.config import Configurator


def main(global_config, **settings):

    """ This function returns a Pyramid WSGI application. """

    config = Configurator(settings=settings)

    # Including internal sub apps
    config.include('users', route_prefix='/api')
    config.include('security')

    config.scan()

    return config.make_wsgi_app()
