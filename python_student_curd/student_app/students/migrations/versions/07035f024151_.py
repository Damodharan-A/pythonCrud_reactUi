"""empty message

Revision ID: 07035f024151
Revises: 4c90e7ab2131
Create Date: 2019-11-28 17:16:16.639072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07035f024151'
down_revision = '4c90e7ab2131'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('end_dt', sa.DateTime(), nullable=True))
    op.add_column('students', sa.Column('start_dt', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'start_dt')
    op.drop_column('students', 'end_dt')
    # ### end Alembic commands ###
