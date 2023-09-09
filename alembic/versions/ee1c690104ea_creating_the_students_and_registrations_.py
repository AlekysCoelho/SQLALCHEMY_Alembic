"""creating the students and registrations tables

Revision ID: ee1c690104ea
Revises: 27cfc1d2a30d
Create Date: 2023-09-08 22:46:44.180614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee1c690104ea'
down_revision: Union[str, None] = '27cfc1d2a30d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id_student', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.PrimaryKeyConstraint('id_student')
    )
    op.create_table('registrations',
    sa.Column('id_student', sa.Integer(), nullable=False),
    sa.Column('id_course', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_course'], ['courses.id_course'], ),
    sa.ForeignKeyConstraint(['id_student'], ['students.id_student'], ),
    sa.PrimaryKeyConstraint('id_student', 'id_course')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('registrations')
    op.drop_table('students')
    # ### end Alembic commands ###
