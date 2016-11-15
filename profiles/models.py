import logging

import sqlalchemy as sa
import sqlalchemy_utils as sa_utils
from sqlalchemy.orm import backref, relationship

from pergunta_camara.utils.models import Base, CreatedUpdatedMixin, get_uuid


logger = logging.getLogger(__name__)


class Profile(Base, CreatedUpdatedMixin):

    __tablename__ = 'profile'

    id = sa.Column(sa.Integer, primary_key=True)
    uuid = sa.Column(
        sa.String(32), nullable=False, unique=True, index=True,
        default=get_uuid
    )

    email = sa.Column(sa.String(200), nullable=False, index=True)

    city = sa.Column(sa.String(200), nullable=True, index=True)
    neighborhood = sa.Column(sa.String(200), nullable=True, index=True)

    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'), index=True)
    user = relationship(
        'User', backref=backref('profiles', lazy='dynamic'),
        foreign_keys=[user_id]
    )


class Councillor(Base, CreatedUpdatedMixin):

    __tablename__ = 'councillor'

    id = sa.Column(sa.Integer, primary_key=True)
    uuid = sa.Column(
        sa.String(32), nullable=False, unique=True, index=True,
        default=get_uuid
    )

    name = sa.Column(sa.String(200), nullable=False, unique=False, index=True)
    phone = sa.Column(sa.String(200), nullable=True)
    email = sa.Column(sa.String(200), nullable=True, unique=False, index=True)
    address = sa.Column(sa.String(200), nullable=True)
    room = sa.Column(sa.String(5), nullable=True)
    floor = sa.Column(sa.String(2), nullable=True)
    url = sa.Column(sa_utils.URLType(), nullable=True)
