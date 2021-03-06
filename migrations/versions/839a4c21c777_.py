"""empty message

Revision ID: 839a4c21c777
Revises: 02360f4baccd
Create Date: 2017-08-11 17:40:22.779946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '839a4c21c777'
down_revision = '02360f4baccd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
