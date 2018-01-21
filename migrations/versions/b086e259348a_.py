"""empty message

Revision ID: b086e259348a
Revises: 526b3c4b6aec
Create Date: 2018-01-16 00:16:51.293084

"""

# revision identifiers, used by Alembic.
revision = 'b086e259348a'
down_revision = '526b3c4b6aec'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('history', sa.Column('complete_description', sa.Text(), nullable=True))
    op.add_column('history', sa.Column('short_description', sa.Text(), nullable=True))
    op.drop_column('history', 'full_description')
    op.drop_column('history', 'home_description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('history', sa.Column('home_description', mysql.VARCHAR(length=80), nullable=True))
    op.add_column('history', sa.Column('full_description', mysql.VARCHAR(length=80), nullable=True))
    op.drop_column('history', 'short_description')
    op.drop_column('history', 'complete_description')
    # ### end Alembic commands ###
