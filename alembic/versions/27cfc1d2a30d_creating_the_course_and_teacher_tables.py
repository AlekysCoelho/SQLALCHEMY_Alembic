"""creating the course and teacher tables

Revision ID: 27cfc1d2a30d
Revises: 
Create Date: 2023-09-08 21:50:55.823934

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '27cfc1d2a30d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teachers',
    sa.Column('id_teacher', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.PrimaryKeyConstraint('id_teacher')
    )
    op.create_table('courses',
    sa.Column('id_course', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('codigo', sa.String(length=3), nullable=False),
    sa.Column('id_teacher', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_teacher'], ['teachers.id_teacher'], ),
    sa.PrimaryKeyConstraint('id_course')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('courses')
    op.drop_table('teachers')
    # ### end Alembic commands ###
