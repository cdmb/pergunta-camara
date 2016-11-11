"""Migration to create user modelling

Revision ID: fd7e42eb6197
Revises:
Create Date: 2016-11-11 01:42:48.805618

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'fd7e42eb6197'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'user',
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('created_ip',
                  sqlalchemy_utils.types.ip_address.IPAddressType(length=50),
                  nullable=True),
        sa.Column('updated', sa.DateTime(), nullable=True),
        sa.Column('updated_ip',
                  sqlalchemy_utils.types.ip_address.IPAddressType(length=50),
                  nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(length=32), nullable=False),
        sa.Column('username', sa.String(length=200), nullable=False),
        sa.Column('password', sa.String(length=200), nullable=True),
        sa.Column('email', sa.String(length=200), nullable=False),
        sa.Column('updated_by_user_id', sa.Integer(), nullable=True),
        sa.Column('created_by_user_id', sa.Integer(), nullable=True),

        sa.ForeignKeyConstraint(['created_by_user_id'], ['user.id'],
                                name=op.f('fk_user_created_by_user_id_user')),
        sa.ForeignKeyConstraint(['updated_by_user_id'], ['user.id'],
                                name=op.f('fk_user_updated_by_user_id_user')),

        sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
        sa.UniqueConstraint('uuid', name=op.f('uq_user_uuid'))
    )

    op.create_index(op.f('ix_user_created'), 'user', ['created'], unique=False)
    op.create_index(op.f('ix_user_created_by_user_id'), 'user',
                    ['created_by_user_id'], unique=False)
    op.create_index(op.f('ix_user_created_ip'), 'user', ['created_ip'],
                    unique=False)

    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    op.create_index(op.f('ix_user_updated'), 'user', ['updated'], unique=False)
    op.create_index(op.f('ix_user_updated_by_user_id'), 'user',
                    ['updated_by_user_id'], unique=False)

    op.create_index(op.f('ix_user_updated_ip'), 'user', ['updated_ip'],
                    unique=False)

    op.create_index(op.f('ix_user_username'), 'user', ['username'],
                    unique=False)


def downgrade():

    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_updated_ip'), table_name='user')
    op.drop_index(op.f('ix_user_updated_by_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_updated'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_index(op.f('ix_user_created_ip'), table_name='user')
    op.drop_index(op.f('ix_user_created_by_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_created'), table_name='user')
    op.drop_table('user')
