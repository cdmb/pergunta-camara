import datetime
import uuid
from unittest import mock

from pergunta_camara.utils import models
from pergunta_camara.tests.base import MinimalTestCase


class UtcNowTestCase(MinimalTestCase):

    def test_ensure_return_is_a_datetime(self):
        self.assertTrue(isinstance(models.get_utc_now(), datetime.datetime))


class UUIDTestCase(MinimalTestCase):

    def test_simple_case(self):

        new_uuid = models.get_uuid()

        self.assertEqual(uuid.UUID(new_uuid).hex, new_uuid)


class CurrentUserTestCase(MinimalTestCase):

    def test_when_has_no_user_in_request(self):

        current_user = models.get_current_user()

        self.assertIsNone(current_user)

    @mock.patch('pergunta_camara.utils.models.get_current_user',
                return_value=42)
    def test_when_has_an_user_in_request(self, *mocks):

        current_user_id = models.get_current_user()

        self.assertEqual(current_user_id, 42)


class CurrentIPTestCase(MinimalTestCase):

    def test_get_current_ip_when_request_object_has_no_attr_client_addr(self):

        current_ip = models.get_current_ip()

        self.assertIsNone(current_ip)

    @mock.patch('pergunta_camara.utils.models.get_current_ip',
                return_value='127.0.0.1')
    def test_get_current_ip_when_request_has_attr_client_addr(self, *mocks):

        current_ip = models.get_current_ip()

        self.assertEqual(current_ip, '127.0.0.1')
