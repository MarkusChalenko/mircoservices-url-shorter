"""02_temp_clear

Revision ID: 6d73ee6b0ded
Revises: 38b2a3ef3449
Create Date: 2024-03-23 20:03:24.694193

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d73ee6b0ded'
down_revision: Union[str, None] = '38b2a3ef3449'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_column('user', 'is_active')
    op.drop_column('user', 'email')
    op.drop_column('user', 'is_superuser')
    op.drop_column('user', 'is_verified')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('email', sa.VARCHAR(length=320), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    # ### end Alembic commands ###
