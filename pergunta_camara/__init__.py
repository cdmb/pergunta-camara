from sqlalchemy import engine_from_config

from pyramid.config import Configurator

from .utils.models import Base, DBSession


def main(global_config, **settings):

    """ This function returns a Pyramid WSGI application. """

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)

    # Including internal sub apps
    config.include('users', route_prefix='/api')
    config.include('.security')

    config.scan()

    return config.make_wsgi_app()
