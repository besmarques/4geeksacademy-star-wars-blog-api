"""empty message

Revision ID: 21ef1d6f36cf
Revises: 63a6d0a9da9e
Create Date: 2022-02-14 19:01:39.645364

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '21ef1d6f36cf'
down_revision = '63a6d0a9da9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('planets', 'image',
               existing_type=mysql.VARCHAR(length=250),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('planets', 'image',
               existing_type=mysql.VARCHAR(length=250),
               nullable=True)
    # ### end Alembic commands ###