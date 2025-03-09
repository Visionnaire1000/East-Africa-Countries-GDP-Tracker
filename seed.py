from sqlalchemy.orm import sessionmaker
from lib.database.models import engine, RevenueSource, GDP, EconomicRankings, calculate_and_populate_gdp_and_rankings

Session = sessionmaker(bind=engine)
session = Session()

revenue_data = [
    {"country": "Kenya", "source": "Agriculture", "revenue_kes": 1500000000000},
    {"country": "Kenya", "source": "Tourism", "revenue_kes": 300000000000},
    {"country": "Tanzania", "source": "Mining", "revenue_kes": 1200000000000},
    {"country": "Tanzania", "source": "Agriculture", "revenue_kes": 800000000000},
    {"country": "Uganda", "source": "Oil & Gas", "revenue_kes": 950000000000},
    {"country": "Uganda", "source": "Manufacturing", "revenue_kes": 600000000000},
    {"country": "Rwanda", "source": "Technology", "revenue_kes": 400000000000},
    {"country": "Rwanda", "source": "Tourism", "revenue_kes": 250000000000},
    {"country": "Burundi", "source": "Coffee Exports", "revenue_kes": 180000000000},
    {"country": "Burundi", "source": "Tea Exports", "revenue_kes": 150000000000},
    {"country": "South Sudan", "source": "Oil Exports", "revenue_kes": 2000000000000},
    {"country": "South Sudan", "source": "Agriculture", "revenue_kes": 500000000000}
]

session.query(RevenueSource).delete()
session.query(GDP).delete()
session.query(EconomicRankings).delete()
session.commit()

for data in revenue_data:
    session.add(RevenueSource(**data))

session.commit()

calculate_and_populate_gdp_and_rankings()

print("Seeding done successfully.")
