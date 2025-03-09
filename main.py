import click
import sys
from sqlalchemy.orm import sessionmaker
from lib.database.models import engine, RevenueSource, GDP, EconomicRankings, calculate_and_populate_gdp_and_rankings

Session = sessionmaker(bind=engine)

def display_menu():
    print("\n===== East Africa Countries GDP Tracker =====")
    print("1. Get Economic Ranking")
    print("2. Get GDP of a Country")
    print("3. Retrieve Revenue Sources")
    print("4. Add a Revenue Source")
    print("5. Delete a Revenue Source")
    print("6. Exit")

def get_ranking():
    session = Session()
    country = input("Enter country name (e.g., Kenya, Uganda): ").strip()
    ranking = session.query(EconomicRankings).filter_by(country=country).first()
    
    if ranking:
        print(f"{country} is ranked {ranking.ranking} in economic power.")
    else:
        print(f"No ranking data found for {country}.")
    
    session.close()

def get_gdp():
    session = Session()
    country = input("Enter country name (e.g., Tanzania, Rwanda): ").strip()
    gdp = session.query(GDP).filter_by(country=country).first()
    
    if gdp:
        print(f"{country}'s GDP: {gdp.gdp_kes} KSH")
    else:
        print(f"No GDP data found for {country}.")
    
    session.close()

def get_revenues():
    session = Session()
    country = input("Enter country name (e.g., Rwanda, Burundi): ").strip()
    sources = session.query(RevenueSource).filter_by(country=country).all()
    
    if sources:
        print(f"Revenue sources for {country}:")
        for source in sources:
            print(f"- {source.source}: {source.revenue_kes} KSH")
    else:
        print(f"No revenue sources found for {country}.")
    
    session.close()

def add_revenue():
    session = Session()
    
    country = input("Enter country name (e.g., Kenya, Tanzania): ").strip()
    source = input("Enter revenue source name (e.g., Taxes, Electric Power): ").strip()
    try:
        revenue_kes = float(input("Enter revenue amount in KSH (e.g., 5000000000, 12000000000): "))
    except ValueError:
        print("Invalid revenue amount. Please enter a number.")
        return

    new_source = RevenueSource(country=country, source=source, revenue_kes=revenue_kes)
    session.add(new_source)
    session.commit()

    print(f"Added revenue source: {source} for {country} with {revenue_kes} KSH.")

    calculate_and_populate_gdp_and_rankings()
    
    session.close()

def delete_revenue():
    session = Session()
    country = input("Enter country name (e.g., Uganda, Rwanda): ").strip()
    source = input("Enter revenue source to delete (e.g., Mining, Exports): ").strip()
    
    revenue = session.query(RevenueSource).filter_by(country=country, source=source).first()
    
    if revenue:
        session.delete(revenue)
        session.commit()
        print(f"Deleted revenue source: {source} for {country}.")
        
        calculate_and_populate_gdp_and_rankings()
    else:
        print(f"Revenue source '{source}' not found for {country}.")
    
    session.close()

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            get_ranking()
        elif choice == "2":
            get_gdp()
        elif choice == "3":
            get_revenues()
        elif choice == "4":
            add_revenue()
        elif choice == "5":
            delete_revenue()
        elif choice == "6":
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
