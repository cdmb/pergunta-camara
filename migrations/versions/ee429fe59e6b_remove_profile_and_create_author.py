"""Remove Profile and create Author

Revision ID: ee429fe59e6b
Revises: 1b8503b61cd2
Create Date: 2016-11-26 12:16:49.066036

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ee429fe59e6b'
down_revision = '1b8503b61cd2'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'author',
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('created_ip', sqlalchemy_utils.types.ip_address.IPAddressType(length=50), nullable=True),  # noqa
        sa.Column('updated', sa.DateTime(), nullable=True),
        sa.Column('updated_ip', sqlalchemy_utils.types.ip_address.IPAddressType(length=50), nullable=True),  # noqa
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(length=32), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('updated_by_user_id', sa.Integer(), nullable=True),
        sa.Column('created_by_user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['created_by_user_id'], ['user.id'], name=op.f('fk_author_created_by_user_id_user')),  # noqa
        sa.ForeignKeyConstraint(['updated_by_user_id'], ['user.id'], name=op.f('fk_author_updated_by_user_id_user')),  # noqa
        sa.PrimaryKeyConstraint('id', name=op.f('pk_author'))
    )

    op.create_index(op.f('ix_author_created'), 'author', ['created'], unique=False)  # noqa
    op.create_index(op.f('ix_author_created_by_user_id'), 'author', ['created_by_user_id'], unique=False)  # noqa
    op.create_index(op.f('ix_author_created_ip'), 'author', ['created_ip'], unique=False)  # noqa
    op.create_index(op.f('ix_author_updated'), 'author', ['updated'], unique=False)  # noqa
    op.create_index(op.f('ix_author_updated_by_user_id'), 'author', ['updated_by_user_id'], unique=False)  # noqa
    op.create_index(op.f('ix_author_updated_ip'), 'author', ['updated_ip'], unique=False)  # noqa
    op.create_index(op.f('ix_author_uuid'), 'author', ['uuid'], unique=True)

    op.drop_index('ix_message_profile_id', table_name='message')
    op.drop_constraint('fk_message_profile_id_profile', 'message', type_='foreignkey')  # noqa
    op.drop_column('message', 'profile_id')
    op.drop_table('profile')

    op.drop_table('councillor')

    op.add_column('message', sa.Column('author_id', sa.Integer(), nullable=True))  # noqa
    op.create_index(op.f('ix_message_author_id'), 'message', ['author_id'], unique=False)  # noqa

    op.create_foreign_key(op.f('fk_message_author_id_author'), 'message', 'author', ['author_id'], ['id'])  # noqa


def downgrade():

    op.create_table(
        'profile',
        sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),  # noqa
        sa.Column('created_ip', sa.VARCHAR(length=50), autoincrement=False, nullable=True),  # noqa
        sa.Column('updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),  # noqa
        sa.Column('updated_ip', sa.VARCHAR(length=50), autoincrement=False, nullable=True),  # noqa
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('uuid', sa.VARCHAR(length=32), autoincrement=False, nullable=False),  # noqa
        sa.Column('email', sa.VARCHAR(length=200), autoincrement=False, nullable=False),  # noqa
        sa.Column('city', sa.VARCHAR(length=200), autoincrement=False, nullable=True),  # noqa
        sa.Column('neighborhood', sa.VARCHAR(length=200), autoincrement=False, nullable=True),  # noqa
        sa.Column('created_by_user_id', sa.INTEGER(), autoincrement=False, nullable=True),  # noqa
        sa.Column('updated_by_user_id', sa.INTEGER(), autoincrement=False, nullable=True),  # noqa
        sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(['created_by_user_id'], ['user.id'], name='fk_profile_created_by_user_id_user'),  # noqa
        sa.ForeignKeyConstraint(['updated_by_user_id'], ['user.id'], name='fk_profile_updated_by_user_id_user'),  # noqa
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_profile_user_id_user'),  # noqa
        sa.PrimaryKeyConstraint('id', name='pk_profile')
    )

    op.create_table(
        'councillor',
        sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),  # noqa
        sa.Column('created_ip', sa.VARCHAR(length=50), autoincrement=False, nullable=True),  # noqa
        sa.Column('updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),  # noqa
        sa.Column('updated_ip', sa.VARCHAR(length=50), autoincrement=False, nullable=True),  # noqa
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('uuid', sa.VARCHAR(length=32), autoincrement=False, nullable=False),  # noqa
        sa.Column('name', sa.VARCHAR(length=200), autoincrement=False, nullable=False),  # noqa
        sa.Column('phone', sa.VARCHAR(length=200), autoincrement=False, nullable=True),  # noqa
        sa.Column('email', sa.VARCHAR(length=200), autoincrement=False, nullable=True),  # noqa
        sa.Column('address', sa.VARCHAR(length=200), autoincrement=False, nullable=True),  # noqa
        sa.Column('room', sa.VARCHAR(length=5), autoincrement=False, nullable=True),  # noqa
        sa.Column('floor', sa.VARCHAR(length=2), autoincrement=False, nullable=True),  # noqa
        sa.Column('url', sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column('updated_by_user_id', sa.INTEGER(), autoincrement=False, nullable=True),  # noqa
        sa.Column('created_by_user_id', sa.INTEGER(), autoincrement=False, nullable=True),  # noqa
        sa.ForeignKeyConstraint(['created_by_user_id'], ['user.id'], name='fk_councillor_created_by_user_id_user'),  # noqa
        sa.ForeignKeyConstraint(['updated_by_user_id'], ['user.id'], name='fk_councillor_updated_by_user_id_user'),  # noqa
        sa.PrimaryKeyConstraint('id', name='pk_councillor')
    )

    op.add_column('message', sa.Column('profile_id', sa.INTEGER(), autoincrement=False, nullable=True))  # noqa
    op.create_foreign_key('fk_message_profile_id_profile', 'message', 'profile', ['profile_id'], ['id'])  # noqa
    op.create_index('ix_message_profile_id', 'message', ['profile_id'], unique=False)  # noqa

    op.drop_constraint(op.f('fk_message_author_id_author'), 'message', type_='foreignkey')  # noqa
    op.drop_index(op.f('ix_message_author_id'), table_name='message')
    op.drop_column('message', 'author_id')

    op.drop_index(op.f('ix_author_uuid'), table_name='author')
    op.drop_index(op.f('ix_author_updated_ip'), table_name='author')
    op.drop_index(op.f('ix_author_updated_by_user_id'), table_name='author')
    op.drop_index(op.f('ix_author_updated'), table_name='author')
    op.drop_index(op.f('ix_author_created_ip'), table_name='author')
    op.drop_index(op.f('ix_author_created_by_user_id'), table_name='author')
    op.drop_index(op.f('ix_author_created'), table_name='author')

    op.drop_table('author')
