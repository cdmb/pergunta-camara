from .resources import MessagesResource


def includeme(config):

    # Messages service
    config.add_route('messages', '/messages', factory=MessagesResource)
