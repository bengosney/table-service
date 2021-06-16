"""empty message.

Revision ID: 38e39c9b294e
Revises: 134e03c50854
Create Date: 2021-06-15 13:52:49.339764
"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "38e39c9b294e"
down_revision = "134e03c50854"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tables",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_tables_id"), "tables", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_tables_id"), table_name="tables")
    op.drop_table("tables")
    # ### end Alembic commands ###
