"""create characters table

Revision ID: 61298763f7e4
Revises: 
Create Date: 2020-10-24 12:29:03.632815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "61298763f7e4"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "characters",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String),
        sa.Column("level", sa.Integer),
        sa.Column("STR", sa.Integer),
        sa.Column("DEX", sa.Integer),
        sa.Column("CON", sa.Integer),
        sa.Column("WIS", sa.Integer),
        sa.Column("INT", sa.Integer),
    )


def downgrade():
    pass
