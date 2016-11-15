from .resources import ProfilesResource


def includeme(config):

    # Profiles service
    config.add_route('profiles', '/profiles', factory=ProfilesResource)
