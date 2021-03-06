"""More voucher work

Revision ID: 972ff3647ce2
Revises: d8ad7870d200
Create Date: 2019-12-15 22:04:34.173384

"""

# revision identifiers, used by Alembic.
revision = '972ff3647ce2'
down_revision = 'd8ad7870d200'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_view', sa.Column('vouchers_only', sa.Boolean(), server_default='False', nullable=False))
    op.add_column('voucher', sa.Column('email', sa.String(), nullable=True))
    op.add_column('voucher', sa.Column('purchases_remaining', sa.Integer(), server_default='1', nullable=False))
    op.create_index(op.f('ix_voucher_email'), 'voucher', ['email'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_voucher_email'), table_name='voucher')
    op.drop_column('voucher', 'purchases_remaining')
    op.drop_column('voucher', 'email')
    op.drop_column('product_view', 'vouchers_only')
    # ### end Alembic commands ###
