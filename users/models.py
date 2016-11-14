import logging

import sqlalchemy as sa
from cryptacular import pbkdf2
from sqlalchemy import orm
from sqlalchemy.orm.exc import NoResultFound

from pergunta_camara.utils.models import Base
from pergunta_camara.utils.models import CreatedUpdatedMixin
from pergunta_camara.utils.models import DBSession
from pergunta_camara.utils.models import get_uuid

logger = logging.getLogger(__name__)


def _get_password_manager():
    return pbkdf2.PBKDF2PasswordManager()


class User(Base, CreatedUpdatedMixin):

    __tablename__ = 'user'

    id = sa.Column(sa.Integer, primary_key=True)
    uuid = sa.Column(
        sa.String(32), nullable=False, unique=True, default=get_uuid
    )

    username = sa.Column(sa.String(200), nullable=False, index=True)
    password_ = sa.Column(sa.String(200))
    email = sa.Column(sa.String(200), nullable=False, index=True)

    def __json__(self, to_ignore=None):
        return {
            c: getattr(self, c)
            for c in self.columns if c not in (to_ignore or [])
        }

    @property
    def columns(self):
        return [c.name for c in self.__table__.columns]

    @property
    def password(self):
        return self.password_

    @password.setter
    def password(self, password):
        self.password_ = _get_password_manager().encode(password)

    password = orm.synonym('password_', descriptor=password)

    def _check_password(self, password_to_check):
        return _get_password_manager().check(self.password, password_to_check)

    @classmethod
    def get_user(cls, username):

        try:
            user = DBSession.query(cls).filter_by(username=username).one()
        except NoResultFound as exc:
            logger.info(
                'No user found for the username: {!r}'.format(username),
                exc_info=exc
            )
            user = None

        return user
