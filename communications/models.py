import sqlalchemy as sa
from sqlalchemy.orm import backref, relationship

from pergunta_camara.utils.models import Base, CreatedUpdatedMixin, get_uuid


class Communication(Base, CreatedUpdatedMixin):

    __tablename__ = 'communication'

    id = sa.Column(sa.Integer, primary_key=True)
    uuid = sa.Column(
        sa.String(32), nullable=False, unique=True, index=True,
        default=get_uuid
    )


class Message(Base, CreatedUpdatedMixin):

    __tablename__ = 'message'

    id = sa.Column(sa.Integer, primary_key=True)
    uuid = sa.Column(
        sa.String(32), nullable=False, unique=True, index=True,
        default=get_uuid
    )

    communication_id = sa.Column(
        sa.Integer, sa.ForeignKey('communication.id'), index=True
    )
    communication = relationship(
        'Communication', backref=backref('messages', lazy='dynamic'),
        foreign_keys=[communication_id]
    )

    profile_id = sa.Column(sa.Integer, sa.ForeignKey('profile.id'), index=True)
    profile = relationship(
        'Profile', backref=backref('messages', lazy='dynamic'),
        foreign_keys=[profile_id]
    )

    state = sa.Column(sa.String(50), nullable=False, unique=False, index=True)

    recipient = sa.Column(
        sa.ARRAY(sa.String, as_tuple=True), nullable=False, unique=False,
        index=True
    )

    subject = sa.Column(sa.String(200), nullable=False, unique=False)

    content = sa.Column(sa.Text(), nullable=False)

    @property
    def signature(self):
        return '--{0}.{1}--'.format(self.communication.uuid, self.uuid)
