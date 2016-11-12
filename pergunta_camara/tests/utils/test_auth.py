import collections
from unittest import mock

from pergunta_camara.tests.base import MinimalTestCase
from pergunta_camara.utils import auth


FakeUser = collections.namedtuple(
    'FakeUser', ('username', 'password', 'check_password')
)


class GetUserInvalidPassword(mock.Mock):

    def __init__(self, *args, **kwargs):

        super(GetUserInvalidPassword, self).__init__(*args, **kwargs)

    def check_password(self, password):
        return False


class AuthenticateUserTestCase(MinimalTestCase):

    @mock.patch.object(auth.User, 'get_user', return_value=None)
    def test_exception_when_username_is_invalid(self, get_user_patched):

        username, password = 'foobarbleh', 'secret'

        with self.assertRaises(auth.InvalidAuthUsername) as cm:
            auth.authenticate_user(username, password)

        exception = cm.exception
        expected_message = 'There is no user for the username {!r}'.format(
            username
        )

        self.assertEqual(str(exception), expected_message)

    @mock.patch.object(auth.User, 'get_user')
    def test_exception_when_password_is_invalid(self, get_user_patched):

        get_user_patched.return_value = GetUserInvalidPassword()

        username, password = 'myusername', '43isnottheanswer'

        with self.assertRaises(auth.InvalidAuthPassword):
            auth.authenticate_user(username, password)

        self.assertTrue(get_user_patched.called)

    @mock.patch.object(auth.User, 'get_user')
    def test_authenticate_with_auth_data_is_valid(self, get_user_patched):

        get_user_patched.return_value = FakeUser(
            username='username',
            password='password',
            check_password=lambda password: True
        )

        result = auth.authenticate_user('username', 'password')

        self.assertTrue(get_user_patched.called)
        self.assertIsInstance(result, FakeUser)
        self.assertEqual(result.username, 'username')
