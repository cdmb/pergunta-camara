import sqlalchemy as sa

from pergunta_camara.utils.models import Base


class User(Base):

    __tablename__ = 'user'

    id = sa.Column(sa.Integer, primary_key=True)
    uuid = sa.Column(sa.String(32), nullable=True, unique=True)
    username = sa.Column(sa.String(200), nullable=False, index=True)
    password_ = sa.Column(sa.String(200))
