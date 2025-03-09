from alembic import op
import sqlalchemy as sa

revision = '0002_create_gdp'
down_revision = '0001_create_revenue_sources'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'gdp',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('country', sa.String(100), nullable=False, unique=True),
        sa.Column('gdp_kes', sa.String(50), nullable=False)
    )

def downgrade():
    op.drop_table('gdp')
