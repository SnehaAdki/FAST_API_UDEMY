"""create an column phone_number

Revision ID: 7e2490e27191
Revises: 
Create Date: 2026-02-05 21:04:59.252465

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e2490e27191'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(),server_default="1234"))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')
