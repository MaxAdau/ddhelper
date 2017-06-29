"""Add date to events

Revision ID: d93da4e0ef22
Revises: cb04a13d70ac
Create Date: 2017-06-28 15:53:25.529156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd93da4e0ef22'
down_revision = 'cb04a13d70ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'date')
    # ### end Alembic commands ###
