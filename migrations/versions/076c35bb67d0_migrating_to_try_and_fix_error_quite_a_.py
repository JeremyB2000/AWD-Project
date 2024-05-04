"""Migrating to try and fix error - quite a few changes

Revision ID: 076c35bb67d0
Revises: 9c71e6b3610e
Create Date: 2024-05-04 20:31:36.041578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '076c35bb67d0'
down_revision = '9c71e6b3610e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('combined_fact_table')
    op.drop_table('ingredient_dimension')
    with op.batch_alter_table('recipe_dimension', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ingredients', sa.String(length=100), nullable=True))
        batch_op.drop_column('instructions')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe_dimension', schema=None) as batch_op:
        batch_op.add_column(sa.Column('instructions', sa.TEXT(), nullable=True))
        batch_op.drop_column('ingredients')

    op.create_table('ingredient_dimension',
    sa.Column('ingredient_id', sa.INTEGER(), nullable=False),
    sa.Column('ingredient_name', sa.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('ingredient_id')
    )
    op.create_table('combined_fact_table',
    sa.Column('fact_id', sa.INTEGER(), nullable=False),
    sa.Column('recipe_id', sa.INTEGER(), nullable=True),
    sa.Column('ingredient_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredient_dimension.ingredient_id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe_dimension.recipe_id'], ),
    sa.PrimaryKeyConstraint('fact_id')
    )
    # ### end Alembic commands ###
