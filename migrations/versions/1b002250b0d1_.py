"""empty message

Revision ID: 1b002250b0d1
Revises: 3f45728e5a4c
Create Date: 2017-06-06 15:48:23.486792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b002250b0d1'
down_revision = '3f45728e5a4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('ca_bonus', sa.Integer(), nullable=True),
    sa.Column('max_dex', sa.Integer(), nullable=True),
    sa.Column('armor_penalty_check', sa.Integer(), nullable=True),
    sa.Column('arcane_spell_fail', sa.Integer(), nullable=True),
    sa.Column('speed_6m', sa.Integer(), nullable=True),
    sa.Column('speed_9m', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('dmg_type', sa.String(), nullable=True),
    sa.Column('cost', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    # ### end Alembic commands ###