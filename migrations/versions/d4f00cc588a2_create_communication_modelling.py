"""Create communication modelling

Revision ID: d4f00cc588a2
Revises: e38590e7f6ca
Create Date: 2016-11-15 14:11:11.348092

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'd4f00cc588a2'
down_revision = 'e38590e7f6ca'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'communication',
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('created_ip', sqlalchemy_utils.types.ip_address.IPAddressType(length=50), nullable=True),  # noqa
        sa.Column('updated', sa.DateTime(), nullable=True),
        sa.Column('updated_ip', sqlalchemy_utils.types.ip_address.IPAddressType(length=50), nullable=True),  # noqa
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(length=32), nullable=False),
        sa.Column('updated_by_user_id', sa.Integer(), nullable=True),
        sa.Column('created_by_user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['created_by_user_id'], ['user.id'], name=op.f('fk_communication_created_by_user_id_user')),  # noqa
        sa.ForeignKeyConstraint(['updated_by_user_id'], ['user.id'], name=op.f('fk_communication_updated_by_user_id_user')),  # noqa
        sa.PrimaryKeyConstraint('id', name=op.f('pk_communication'))
    )

    op.create_index(op.f('ix_communication_created'), 'communication', ['created'], unique=False)  # noqa
    op.create_index(op.f('ix_communication_created_by_user_id'), 'communication', ['created_by_user_id'], unique=False)  # noqa
    op.create_index(op.f('ix_communication_created_ip'), 'communication', ['created_ip'], unique=False)  # noqa
    op.create_index(op.f('ix_communication_updated'), 'communication', ['updated'], unique=False)  # noqa
    op.create_index(op.f('ix_communication_updated_by_user_id'), 'communication', ['updated_by_user_id'], unique=False)  # noqa
    op.create_index(op.f('ix_communication_updated_ip'), 'communication', ['updated_ip'], unique=False)  # noqa
    op.create_index(op.f('ix_communication_uuid'), 'communication', ['uuid'], unique=True)  # noqa

    op.create_table(
        'message',
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('created_ip', sqlalchemy_utils.types.ip_address.IPAddressType(length=50), nullable=True),  # noqa
        sa.Column('updated', sa.DateTime(), nullable=True),
        sa.Column('updated_ip', sqlalchemy_utils.types.ip_address.IPAddressType(length=50), nullable=True),  # noqa
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(length=32), nullable=False),
        sa.Column('communication_id', sa.Integer(), nullable=True),
        sa.Column('profile_id', sa.Integer(), nullable=True),
        sa.Column('state', sa.String(length=50), nullable=False),
        sa.Column('recipient', sa.ARRAY(sa.String(), as_tuple=True), nullable=False),  # noqa
        sa.Column('subject', sa.String(length=200), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('updated_by_user_id', sa.Integer(), nullable=True),
        sa.Column('created_by_user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['communication_id'], ['communication.id'], name=op.f('fk_message_communication_id_communication')),  # noqa
        sa.ForeignKeyConstraint(['created_by_user_id'], ['user.id'], name=op.f('fk_message_created_by_user_id_user')),  # noqa
        sa.ForeignKeyConstraint(['profile_id'], ['profile.id'], name=op.f('fk_message_profile_id_profile')),  # noqa
        sa.ForeignKeyConstraint(['updated_by_user_id'], ['user.id'], name=op.f('fk_message_updated_by_user_id_user')),  # noqa
        sa.PrimaryKeyConstraint('id', name=op.f('pk_message'))
    )

    op.create_index(op.f('ix_message_communication_id'), 'message', ['communication_id'], unique=False)  # noqa
    op.create_index(op.f('ix_message_created'), 'message', ['created'], unique=False)  # noqa
    op.create_index(op.f('ix_message_created_by_user_id'), 'message', ['created_by_user_id'], unique=False)  # noqa
    op.create_index(op.f('ix_message_created_ip'), 'message', ['created_ip'], unique=False)  # noqa
    op.create_index(op.f('ix_message_profile_id'), 'message', ['profile_id'], unique=False)  # noqa
    op.create_index(op.f('ix_message_recipient'), 'message', ['recipient'], unique=False)  # noqa
    op.create_index(op.f('ix_message_state'), 'message', ['state'], unique=False)  # noqa
    op.create_index(op.f('ix_message_updated'), 'message', ['updated'], unique=False)  # noqa
    op.create_index(op.f('ix_message_updated_by_user_id'), 'message', ['updated_by_user_id'], unique=False)  # noqa
    op.create_index(op.f('ix_message_updated_ip'), 'message', ['updated_ip'], unique=False)  # noqa
    op.create_index(op.f('ix_message_uuid'), 'message', ['uuid'], unique=True)


def downgrade():

    op.drop_index(op.f('ix_message_uuid'), table_name='message')
    op.drop_index(op.f('ix_message_updated_ip'), table_name='message')
    op.drop_index(op.f('ix_message_updated_by_user_id'), table_name='message')
    op.drop_index(op.f('ix_message_updated'), table_name='message')
    op.drop_index(op.f('ix_message_state'), table_name='message')
    op.drop_index(op.f('ix_message_recipient'), table_name='message')
    op.drop_index(op.f('ix_message_profile_id'), table_name='message')
    op.drop_index(op.f('ix_message_created_ip'), table_name='message')
    op.drop_index(op.f('ix_message_created_by_user_id'), table_name='message')
    op.drop_index(op.f('ix_message_created'), table_name='message')
    op.drop_index(op.f('ix_message_communication_id'), table_name='message')

    op.drop_table('message')

    op.drop_index(op.f('ix_communication_uuid'), table_name='communication')
    op.drop_index(op.f('ix_communication_updated_ip'), table_name='communication')  # noqa
    op.drop_index(op.f('ix_communication_updated_by_user_id'), table_name='communication')  # noqa
    op.drop_index(op.f('ix_communication_updated'), table_name='communication')
    op.drop_index(op.f('ix_communication_created_ip'), table_name='communication')  # noqa
    op.drop_index(op.f('ix_communication_created_by_user_id'), table_name='communication')  # noqa
    op.drop_index(op.f('ix_communication_created'), table_name='communication')

    op.drop_table('communication')
