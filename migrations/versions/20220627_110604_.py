"""empty message

Revision ID: 2cb2ba3c88f6
Revises:
Create Date: 2022-06-27 11:06:04.109416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cb2ba3c88f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('settled', sa.Boolean(create_constraint='false'), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('hashed_password', sa.String(length=102), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bill_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=2000), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['bill_id'], ['bills.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_bills',
    sa.Column('users', sa.Integer(), nullable=False),
    sa.Column('bills', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['bills'], ['bills.id'], ),
    sa.ForeignKeyConstraint(['users'], ['users.id'], ),
    sa.PrimaryKeyConstraint('users', 'bills')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_bills')
    op.drop_table('comments')
    op.drop_table('users')
    op.drop_table('bills')
    # ### end Alembic commands ###
