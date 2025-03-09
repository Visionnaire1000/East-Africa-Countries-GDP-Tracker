from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func

Base = declarative_base()

engine = create_engine("sqlite:///gdp_tracker.db")
Session = sessionmaker(bind=engine)

class RevenueSource(Base):
    __tablename__ = "revenue_sources"
    
    id = Column(Integer, primary_key=True)
    country = Column(String, ForeignKey("gdp.country"), nullable=False)
    source = Column(String, nullable=False)
    revenue_kes = Column(Float, nullable=False)

    gdp = relationship("GDP", back_populates="revenue_sources")

class GDP(Base):
    __tablename__ = "gdp"
    
    id = Column(Integer, primary_key=True)
    country = Column(String, unique=True, nullable=False)
    gdp_kes = Column(Float, nullable=False)

    revenue_sources = relationship("RevenueSource", back_populates="gdp")
    ranking = relationship("EconomicRankings", uselist=False, back_populates="gdp")

class EconomicRankings(Base):
    __tablename__ = "economic_rankings"
    
    id = Column(Integer, primary_key=True)
    country = Column(String, ForeignKey("gdp.country"), unique=True, nullable=False)
    ranking = Column(Integer, nullable=False)  

    gdp = relationship("GDP", back_populates="ranking")

def calculate_and_populate_gdp_and_rankings():
    session = Session()
    
    try:
        print("Checking if revenue data exists...")
        revenue_exists = session.query(RevenueSource).first()
        if not revenue_exists:
            print("No revenue data found. Skipping GDP calculation.")
            return

        print("Calculating GDP values...")
        
        print("Deleting old GDP and rankings...")
        session.query(GDP).delete()
        session.query(EconomicRankings).delete()
        session.commit()

        print("Inserting new GDP values...")
        country_gdp_map = {}
        
        for country, total_revenue in session.query(
            RevenueSource.country, func.sum(RevenueSource.revenue_kes)
        ).group_by(RevenueSource.country).all():
            gdp = GDP(country=country, gdp_kes=total_revenue)
            session.add(gdp)
            country_gdp_map[country] = total_revenue
            print(f"{country} -> GDP: {total_revenue}")

        session.commit()

        print("Fetching updated GDPs for ranking...")
        ranked_countries = sorted(country_gdp_map.items(), key=lambda x: x[1], reverse=True)

        print("Assigning economic rankings...")
        for ranking, (country, gdp_kes) in enumerate(ranked_countries, start=1):
            ranking_entry = EconomicRankings(country=country, ranking=ranking) 
            session.add(ranking_entry)

        session.commit()
        print("GDP calculation and ranking update completed successfully.")

    except Exception as e:
        print(f"Error calculating GDP and rankings: {e}")
        session.rollback()
    
    finally:
        session.close()
