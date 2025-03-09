from alembic import op
import sqlalchemy as sa

revision = '0001_create_revenue_sources'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'revenue_sources',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('country', sa.String(100), nullable=False),
        sa.Column('source', sa.String(255), nullable=False),
        sa.Column('revenue_kes', sa.String(50), nullable=False)
    )

def downgrade():
    op.drop_table('revenue_sources')
