import datetime
import logging
import uuid

import sqlalchemy as sa
import sqlalchemy_utils as sa_utils

from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker, relation
from sqlalchemy.schema import MetaData
from zope.sqlalchemy import ZopeTransactionExtension

from pyramid.threadlocal import get_current_request


logger = logging.getLogger(__name__)


# Recommended naming convention used by Alembic, as various different database
# providers will autogenerate vastly different names making migrations more
# difficult. See: http://alembic.zzzcomputing.com/en/latest/naming.html
NAMING_CONVENTION = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
metadata = MetaData(naming_convention=NAMING_CONVENTION)
Base = declarative_base(metadata=metadata)


def get_utc_now():
    return datetime.datetime.utcnow()


def get_uuid():
    return uuid.uuid4().hex


def get_current_ip():

    try:
        return get_current_request().client_addr
    except AttributeError as exc:
        logger.exception('Error trying to get the current ip.', exc_info=exc)


def get_current_user():

    try:
        return get_current_request().user.id
    except AttributeError as exc:
        logger.exception('Error trying to get the current user', exc_info=exc)


class CreatedUpdatedMixin:

    """Provides created and updated attributes"""

    created = sa.Column(sa.DateTime, default=get_utc_now, index=True)
    created_ip = sa.Column(
        sa_utils.IPAddressType, default=get_current_ip, nullable=True,
        index=True
    )

    updated = sa.Column(
        sa.DateTime, default=get_utc_now, onupdate=get_utc_now, index=True
    )
    updated_ip = sa.Column(
        sa_utils.IPAddressType, default=get_current_ip,
        onupdate=get_current_ip, nullable=True, index=True
    )

    @declared_attr
    def created_by_user_id(self):
        return sa.Column(
            sa.Integer, sa.ForeignKey('user.id'), nullable=True,
            default=get_current_user, index=True
        )

    @declared_attr
    def created_by_user(cls):
        return relation(
            'User',
            primaryjoin='{}.created_by_user_id == User.id'.format(cls.__name__)
        )

    @declared_attr
    def updated_by_user_id(self):
        return sa.Column(
            sa.Integer, sa.ForeignKey('user.id'), nullable=True,
            default=get_current_user, onupdate=get_current_user, index=True
        )

    @declared_attr
    def updated_by_user(cls):
        return relation(
            'User',
            primaryjoin='{}.updated_by_user_id == User.id'.format(cls.__name__)
        )
