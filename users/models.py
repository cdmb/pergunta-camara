import sqlalchemy as sa

from pergunta_camara.utils.models import Base, CreatedUpdatedMixin


class User(Base, CreatedUpdatedMixin):

    __tablename__ = 'user'

    id = sa.Column(sa.Integer, primary_key=True)
    uuid = sa.Column(sa.String(32), nullable=False, unique=True)

    username = sa.Column(sa.String(200), nullable=False, index=True)
    password = sa.Column(sa.String(200))
    email = sa.Column(sa.String(200), nullable=False, index=True)
