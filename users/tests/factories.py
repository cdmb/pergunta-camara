import factory

# from pergunta_camara.utils.models import DBSession
from users.models import User


class UserFactory(factory.Factory):

    class Meta:
        model = User

    # FACTORY_FOR = User
    # FACTORY_SESSION = DBSession

    username = 'user@test.com'
    email = 'user@test.com'
