from alembic import op
import sqlalchemy as sa

revision = '0003_create_economic_rankings'
down_revision = '0002_create_gdp'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'economic_rankings',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('country', sa.String(100), nullable=False, unique=True),
        sa.Column('ranking', sa.Integer, nullable=False)
    )

def downgrade():
    op.drop_table('economic_rankings')
