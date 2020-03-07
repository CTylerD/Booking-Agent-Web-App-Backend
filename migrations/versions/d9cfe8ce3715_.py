"""empty message

Revision ID: d9cfe8ce3715
Revises: f3f1aa94c0a2
Create Date: 2020-02-29 19:00:56.644917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9cfe8ce3715'
down_revision = 'f3f1aa94c0a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_link', sa.String(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('time', sa.Time(), nullable=True),
    sa.Column('happened', sa.Boolean(), nullable=True),
    sa.Column('artist', sa.String(), nullable=True),
    sa.Column('venue', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['artist'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['venue'], ['venues.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shows')
    # ### end Alembic commands ###