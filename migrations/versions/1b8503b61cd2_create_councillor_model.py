"""Create Councillor model

Revision ID: 1b8503b61cd2
Revises: d4f00cc588a2
Create Date: 2016-11-15 18:20:41.180677

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '1b8503b61cd2'
down_revision = 'd4f00cc588a2'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'councillor',
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('created_ip', sqlalchemy_utils.types.ip_address.IPAddressType(length=50), nullable=True),  # noqa
        sa.Column('updated', sa.DateTime(), nullable=True),
        sa.Column('updated_ip', sqlalchemy_utils.types.ip_address.IPAddressType(length=50), nullable=True),  # noqa
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(length=32), nullable=False),
        sa.Column('name', sa.String(length=200), nullable=False),
        sa.Column('phone', sa.String(length=200), nullable=True),
        sa.Column('email', sa.String(length=200), nullable=True),
        sa.Column('address', sa.String(length=200), nullable=True),
        sa.Column('room', sa.String(length=5), nullable=True),
        sa.Column('floor', sa.String(length=2), nullable=True),
        sa.Column('url', sqlalchemy_utils.types.url.URLType(), nullable=True),
        sa.Column('updated_by_user_id', sa.Integer(), nullable=True),
        sa.Column('created_by_user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['created_by_user_id'], ['user.id'], name=op.f('fk_councillor_created_by_user_id_user')),  # noqa
        sa.ForeignKeyConstraint(['updated_by_user_id'], ['user.id'], name=op.f('fk_councillor_updated_by_user_id_user')),  # noqa
        sa.PrimaryKeyConstraint('id', name=op.f('pk_councillor'))
    )

    op.create_index(op.f('ix_councillor_created'), 'councillor', ['created'], unique=False)  # noqa
    op.create_index(op.f('ix_councillor_created_by_user_id'), 'councillor', ['created_by_user_id'], unique=False)  # noqa
    op.create_index(op.f('ix_councillor_created_ip'), 'councillor', ['created_ip'], unique=False)  # noqa
    op.create_index(op.f('ix_councillor_email'), 'councillor', ['email'], unique=False)  # noqa
    op.create_index(op.f('ix_councillor_name'), 'councillor', ['name'], unique=False)  # noqa
    op.create_index(op.f('ix_councillor_updated'), 'councillor', ['updated'], unique=False)  # noqa
    op.create_index(op.f('ix_councillor_updated_by_user_id'), 'councillor', ['updated_by_user_id'], unique=False)  # noqa
    op.create_index(op.f('ix_councillor_updated_ip'), 'councillor', ['updated_ip'], unique=False)  # noqa
    op.create_index(op.f('ix_councillor_uuid'), 'councillor', ['uuid'], unique=True)  # noqa


def downgrade():

    op.drop_index(op.f('ix_councillor_uuid'), table_name='councillor')
    op.drop_index(op.f('ix_councillor_updated_ip'), table_name='councillor')
    op.drop_index(op.f('ix_councillor_updated_by_user_id'), table_name='councillor')  # noqa
    op.drop_index(op.f('ix_councillor_updated'), table_name='councillor')
    op.drop_index(op.f('ix_councillor_name'), table_name='councillor')
    op.drop_index(op.f('ix_councillor_email'), table_name='councillor')
    op.drop_index(op.f('ix_councillor_created_ip'), table_name='councillor')
    op.drop_index(op.f('ix_councillor_created_by_user_id'), table_name='councillor')  # noqa
    op.drop_index(op.f('ix_councillor_created'), table_name='councillor')

    op.drop_table('councillor')
