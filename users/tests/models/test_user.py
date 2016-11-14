from unittest import mock

from sqlalchemy import exc

from pergunta_camara.tests.base import BaseTestCase, MinimalTestCase
from pergunta_camara.utils.models import DBSession
from users.models import _get_password_manager, logger
from users.tests.factories import User, UserFactory


class PasswordManagerTestCase(MinimalTestCase):

    def test_encode(self):

        password = 'mysecret'

        password_manager = _get_password_manager()

        self.assertNotEqual(password, password_manager.encode(password))

    def test_check(self):

        password = 'mysecret'

        password_manager = _get_password_manager()

        encoded_password = password_manager.encode(password)

        self.assertTrue(password_manager.check(encoded_password, password))


class UserTestCase(BaseTestCase):

    def test_get_columns(self):

        user = User()

        self.assertListEqual(
            user.columns, [c.name for c in user.__table__.columns]
        )

    def test_dunder_json_all_attributes(self):

        user = User()

        expected_result = {c: getattr(user, c) for c in user.columns}

        self.assertDictEqual(user.__json__(), expected_result)

    def test_dunder_json_and_ignore_some_columns(self):

        user = User(email='foo@bar.com')

        to_ignore = 'id', 'uuid', 'password'

        expected_result = {
            c: getattr(user, c) for c in user.columns if c not in to_ignore
        }

        self.assertDictEqual(user.__json__(to_ignore), expected_result)

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

    def test_password_is_not_stored_as_plain_text(self):

        user = UserFactory(password='test123')
        DBSession.add(user)
        DBSession.flush()

        user = DBSession.query(User).one()

        self.assertNotEqual(user.password, 'test123')

    @mock.patch.object(logger, 'info')
    def test_get_user_when_the_username_is_invalid(self, info_patched):

        username = 'foobarbleh'

        user = User.get_user(username)

        # A message log about the exception NoResultFound
        self.assertTrue(info_patched.called)

        self.assertIsNone(user)

    @mock.patch.object(logger, 'info')
    def test_get_user_when_the_username_is_valid(self, info_patched):

        username = 'ada lovelace'

        user = UserFactory(username=username)
        DBSession.add(user)
        DBSession.flush()

        result = User.get_user(username)

        self.assertIsInstance(result, User)

        self.assertEqual(result.email, user.email)
        self.assertEqual(result.uuid, user.uuid)

    def test_check_user_password(self):

        user = UserFactory(password='42istheanswer')
        DBSession.add(user)
        DBSession.flush()

        self.assertTrue(user._check_password('42istheanswer'))
