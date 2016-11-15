from .views.routes import includeme as views_include


def includeme(config):

    config.include(views_include)
    config.scan()
