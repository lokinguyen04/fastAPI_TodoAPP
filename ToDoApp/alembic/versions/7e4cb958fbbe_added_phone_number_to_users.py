"""Added phone_number to Users

Revision ID: 7e4cb958fbbe
Revises: 15ed56af81f3
Create Date: 2025-03-25 13:58:22.711463

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e4cb958fbbe'
down_revision: Union[str, None] = '15ed56af81f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###
