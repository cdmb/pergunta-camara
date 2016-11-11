from sqlalchemy import exc

from pergunta_camara.tests.base import BaseTestCase
from pergunta_camara.utils.models import DBSession
from users.tests.factories import UserFactory


class UserTestCase(BaseTestCase):

    def test_exceptions_when_username_is_none(self):

        user = UserFactory(username=None)
        DBSession.add(user)

        with self.assertRaises(exc.IntegrityError):
            DBSession.flush()

    def test_exceptions_when_email_is_none(self):

        user = UserFactory(email=None)
        DBSession.add(user)

        with self.assertRaises(exc.IntegrityError):
            DBSession.flush()
