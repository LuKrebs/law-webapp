"""empty message

Revision ID: b9124ae4a981
Revises: b086e259348a
Create Date: 2018-01-16 00:22:22.302221

"""

# revision identifiers, used by Alembic.
revision = 'b9124ae4a981'
down_revision = 'b086e259348a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('history', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('history', 'active')
    # ### end Alembic commands ###
