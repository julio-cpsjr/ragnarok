"""empty message

Revision ID: 89442d005b1d
Revises: 
Create Date: 2024-04-16 13:06:05.448709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89442d005b1d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('cpf', sa.Integer(), nullable=True),
    sa.Column('hostname', sa.String(), nullable=True),
    sa.Column('machine_model', sa.String(), nullable=True),
    sa.Column('mac_address', sa.Integer(), nullable=True),
    sa.Column('area', sa.String(), nullable=True),
    sa.Column('antivirus', sa.String(), nullable=True),
    sa.Column('atualizacao', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('name_job', sa.String(), nullable=True),
    sa.Column('confirm', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###