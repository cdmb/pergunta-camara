import os
import unittest

import transaction
from pyramid_mailer import get_mailer
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from webtest import TestApp
from zope.sqlalchemy import ZopeTransactionExtension

from paste.deploy.loadwsgi import appconfig
from pyramid import testing

from pergunta_camara import main as main_app
from pergunta_camara.utils.models import DBSession


class TestCase(unittest.TestCase):

    create_db = False
    create_app = False
    create_settings = False
    add_basic_configs = False

    @classmethod
    def setUpClass(cls):
        super(TestCase, cls).setUpClass()

        if cls.create_settings:

            settings_file = 'test.ini' if not os.getenv('CI_ENV') else 'ci.ini'

            cls.settings = appconfig('config:' + os.path.join(
                os.path.dirname(__file__), '../../', settings_file
            ))
            cls.config = testing.setUp(settings=cls.settings)

        if cls.create_db:

            cls.engine = engine_from_config(cls.settings, prefix='sqlalchemy.')
            cls.Session = sessionmaker(
                autoflush=False, extension=ZopeTransactionExtension()
            )

        if cls.add_basic_configs:
            cls.create_basic_configs_via_class()

        if cls.create_app:
            cls.app = main_app({}, **cls.settings)

    @classmethod
    def tearDownClass(cls):
        super(TestCase, cls).tearDownClass()

        if cls.create_db:
            cls.Session.close_all()
            cls.engine.dispose()

        if cls.create_settings:
            testing.tearDown()

    def setUp(self):
        super(TestCase, self).setUp()

        if self.create_db:
            self._connection = self.engine.connect()
            self.transaction = self._connection.begin_nested()
            DBSession.configure(bind=self._connection)

        if self.create_app:
            self.app = TestApp(self.app)
            registry = self.app.app.registry
            self.mailer = get_mailer(registry)
            self.mailer.outbox = []

    def tearDown(self):
        super(TestCase, self).tearDown()

        if self.create_db:

            self.transaction.rollback()
            DBSession.remove()

            transaction.abort()
            self._connection.close()

        if self.create_app:
            self.mailer.outbox = []

    @classmethod
    def create_basic_configs_via_class(cls):

        if not cls.create_settings:
            raise RuntimeError(
                'cls.config is not available. Consider using SettingsTestCase.'
            )

        cls.config.include('pyramid_mailer.testing')

    def create_basic_configs(self):
        self.__class__.create_basic_configs_via_class()


class MinimalTestCase(TestCase):
    pass


class BaseTestCase(MinimalTestCase):

    create_db = True
    create_settings = True
    add_basic_configs = True


class FunctionalTestCase(BaseTestCase):

    create_app = True
