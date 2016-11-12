import logging

from pergunta_camara.models import User


logger = logging.getLogger(__name__)


class InvalidAuthUsername(ValueError):
    pass


class InvalidAuthPassword(ValueError):
    pass


def authenticate_user(username, password):

    user = User.get_user(username)

    if not user:

        logger.warning(
            '[authenticate_user] Invalid username: {!r}'.format(username)
        )

        raise InvalidAuthUsername(
            'There is no user for the username {!r}'.format(username)
        )

    if not user.check_password(password):

        logger.warning(
            '[authenticate_user] Invalid password: {!r}'.format(password)
        )

        raise InvalidAuthPassword()

    return user
