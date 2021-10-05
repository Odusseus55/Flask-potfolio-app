"""add current price to stocks table

Revision ID: 3aa3964ffac5
Revises: f1ba66565895
Create Date: 2021-02-24 19:20:34.170912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3aa3964ffac5'
down_revision = 'f1ba66565895'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stocks', sa.Column('current_price', sa.Integer(), nullable=True))
    op.add_column('stocks', sa.Column('current_price_date', sa.DateTime(), nullable=True))
    op.add_column('stocks', sa.Column('position_value', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'stocks', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stocks', type_='foreignkey')
    op.drop_column('stocks', 'position_value')
    op.drop_column('stocks', 'current_price_date')
    op.drop_column('stocks', 'current_price')
    # ### end Alembic commands ###